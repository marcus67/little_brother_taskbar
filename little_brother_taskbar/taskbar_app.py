# -*- coding: utf-8 -*-

# Copyright (C) 2019  Marcus Rickert
#
# See https://github.com/marcus67/little_brother_taskbar
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
import datetime
import locale
import os.path
import threading
from typing import Optional

import wx
import wx.adv

from little_brother_taskbar import configuration_model, button_info, constants
from little_brother_taskbar import status_connector
from little_brother_taskbar import taskbar
from little_brother_taskbar.status_frame import StatusFrame
from little_brother_taskbar.user_status import UserStatus
from python_base_app import audio_handler
from python_base_app import base_app
from python_base_app import configuration
from python_base_app import locale_helper
from python_base_app import tools

UTF_LOUDSPEAKER = "🔊"
UTF_MUTED_LOUDSPEAKER = "🔇"
ADD_MINUTE_LABEL_FORMAT_STRING = "+{minutes} min."


def get_argument_parser(p_app_name):
    parser = base_app.get_argument_parser(p_app_name=p_app_name)
    parser.add_argument('--server-url', dest='server_url', action='store',
                        help='Set the URL to retrieve user status',
                        default="http://localhost:5555")
    parser.add_argument('--username', dest='username', action='store',
                        help='Set the username to request the status for')
    parser.add_argument('--locale', dest='locale', action='store',
                        help='Set the locale string (e.g. de_DE)')
    parser.add_argument('--speech-engine', dest='speech_engine', action='store',
                        help='Set the speech engine for MP3 generation of notification messages',
                        choices=['google', 'external'])
    return parser


class App(base_app.BaseApp):

    def __init__(self, p_pid_file, p_arguments, p_app_name):
        """Main class for the application LittleBrotherTaskbar."""
        super(App, self).__init__(p_pid_file=p_pid_file, p_arguments=p_arguments, p_app_name=p_app_name,
                                  p_dir_name='.')

        self._wx_app = wx.App(useBestVisual=True)
        self._app_config : Optional[configuration_model.TaskBarAppConfigModel] = None
        self._status_frame: Optional[StatusFrame] = None
        self._status_connector = None
        self._audio_handler = None
        self._taskbar_process = None
        self._username = None
        self._latest_notification = None
        self._locale = None
        self._last_status_update = tools.get_current_time()
        self._warning_time_without_send_events = None
        self._maximum_time_without_send_events = None
        self._user_status: UserStatus = UserStatus()
        self._window_title = configuration_model.APP_NAME
        self._earliest_button_activation : datetime.datetime = tools.get_current_time()

        self.check_user_configuration_file()

    def prepare_configuration(self, p_configuration):

        status_connector_section = status_connector.StatusConnectorConfigModel()
        p_configuration.add_section(status_connector_section)

        audio_handler_section = audio_handler.AudioHandlerConfigModel()
        audio_handler_section.spool_dir = "/tmp"
        p_configuration.add_section(audio_handler_section)

        self._app_config = configuration_model.TaskBarAppConfigModel()
        p_configuration.add_section(self._app_config)

        return super(App, self).prepare_configuration(p_configuration=p_configuration)

    def set_locale(self, p_locale):

        if self._locale is None or p_locale != self._locale:
            if self._locale is None:
                fmt = "Using locale '{locale}'"

            else:
                fmt = "Switching to locale '{locale}'"

            self._logger.info(fmt.format(locale=p_locale))
            self._locale = p_locale

    def speak_status(self, p_user_status):

        self.speak_notification(p_notification=p_user_status.notification, p_locale=p_user_status.locale)

    def speak_notification(self, p_notification, p_locale=None):

        if p_locale is None:
            p_locale = self._locale

        if self._audio_handler is not None:
            if p_notification is not None and p_notification != self._latest_notification:
                self._audio_handler.notify(p_text=p_notification, p_locale=p_locale)
                self._latest_notification = p_notification

    def clear_notification(self):

        self._latest_notification = None

    def update_status(self):

        self._logger.debug("update_status")

        if self._status_frame is None:
            return

        user_status = self._status_connector.request_status(p_username=self._username)

        font_size = self._app_config.status_message_font_size
        color = self._color_normal_mode
        color_foreground = self._color_normal_mode_foreground
        text = None

        if user_status is None:
            self.clear_notification()

        else:
            if isinstance(user_status, str):
                time_without_status_update = int(
                    (tools.get_current_time() - self._last_status_update).total_seconds() / 10) * 10

                notification = None

                if self._warning_time_without_send_events is not None and self._maximum_time_without_send_events is not None:
                    if self._warning_time_without_send_events <= time_without_status_update < self._maximum_time_without_send_events:
                        time_remaining = self._maximum_time_without_send_events - time_without_status_update
                        msg = self._("Restore network or you will be logged out in {time_remaining} seconds.")
                        text = self._(msg.format(time_without_status_update=time_without_status_update,
                                                 time_remaining=time_remaining))
                        notification = text

                    elif time_without_status_update >= self._maximum_time_without_send_events:
                        msg = self._(
                            "No network for at least {maximum_time_without_send_events} seconds. You will be logged out immediately.")
                        text = self._(
                            msg.format(maximum_time_without_send_events=self._maximum_time_without_send_events))
                        notification = text

                else:
                    text = user_status

                if text is not None:
                    font_size = self._app_config.error_message_font_size
                    color = self._color_error_message
                    color_foreground = self._color_error_message_foreground

                    if self._app_config.enable_spoken_notifications:
                        self.speak_notification(p_notification=notification)

                    else:
                        self.clear_notification()

            else:
                self._user_status = user_status
                self.set_locale(p_locale=user_status.locale)
                self._warning_time_without_send_events = user_status.warning_time_without_send_events
                self._maximum_time_without_send_events = user_status.maximum_time_without_send_events
                self._last_status_update = tools.get_current_time()

                font_size = self._app_config.status_message_font_size

                if not user_status.logged_in:
                    color = self._color_warning_message
                    color_foreground = self._color_warning_message_foreground
                    font_size = self._app_config.error_message_font_size
                    fmt = self._("User '{username}' not logged in")
                    text = fmt.format(username=self._username)
                    self.clear_notification()

                elif user_status.activity_allowed:
                    if user_status.minutes_left_in_session is not None:
                        fmt = self._("Time left:\n{minutes} minutes")
                        text = fmt.format(minutes=user_status.minutes_left_in_session)

                        if user_status.minutes_left_in_session <= self._app_config.warning_minutes_approaching_logout:
                            color = self._color_approaching_logout
                            color_foreground = self._color_approaching_logout_foreground

                            if self._app_config.show_window_when_approaching_logout:
                                self.show_status_frame(True)

                        else:
                            color = self._color_normal_mode
                            color_foreground = self._color_normal_mode_foreground

                    else:
                        text = self._("Unlimited Time")
                        color = self._color_normal_mode
                        color_foreground = self._color_normal_mode_foreground

                else:
                    color = self._color_warning_message
                    color_foreground = self._color_normal_mode_foreground
                    text = self._("No Activity Allowed")

                if user_status.logged_in and self._app_config.enable_spoken_notifications:
                    self.speak_status(p_user_status=user_status)

                self.set_time_extension_buttons()
                self.set_frame_size_and_title()


            if text is not None:
                # https://stackoverflow.com/questions/14320836/wxpython-pango-error-when-using-a-while-true-loop-in-a-thread
                #self._logger.info("Before CallAfter")
                if self._user_status.optional_time_available is not None:
                    small_text_format = self._("(Optional time available: {minutes})")
                    small_text = small_text_format.format(minutes=self._user_status.optional_time_available)

                else:
                    small_text = None
                wx.CallAfter(self._status_frame.redraw_text, text, small_text, font_size, color, color_foreground)
                #self._logger.info("After CallAfter")

    def set_time_extension_buttons(self):

        time_extension_buttons_active = self._user_status.optional_time_available is not None \
                                and tools.get_current_time() > self._earliest_button_activation \
                                and self._user_status.minutes_left_in_session is not None

        button_infos = [ button_info.ButtonInfo(p_active=time_extension_buttons_active and
                                                interval <= self._user_status.optional_time_available,
                                                p_minutes=interval)
                         for interval in self._app_config.add_time_intervals ]

        wx.CallAfter(self._status_frame.set_buttons,
                     p_time_extension_active=self._user_status.optional_time_available is not None,
                     p_button_infos=button_infos)

    def get_window_size(self):

        if self._user_status.optional_time_available is not None:
            window_height = (self._app_config.window_height - constants.DEFAULT_WINDOW_HEIGHT_INCREASE_FOR_TIME_EXTENSION) * constants.DEFAULT_WINDOW_HEIGHT_FACTOR_FOR_TIME_EXTENSION + constants.DEFAULT_WINDOW_HEIGHT_INCREASE_FOR_TIME_EXTENSION

        else:
            window_height = self._app_config.window_height - constants.DEFAULT_WINDOW_HEIGHT_INCREASE_FOR_TIME_EXTENSION

        return (self._app_config.window_width, window_height)

    def set_frame_size_and_title(self):

        wx.CallAfter(self._status_frame.update, self.get_window_size(), self._window_title)

    def evaluate_configuration(self):

        if self._app_config.enable_spoken_notifications:
            self._window_title = configuration_model.APP_NAME + " " + UTF_LOUDSPEAKER

        else:
            self._window_title = configuration_model.APP_NAME + " " + UTF_MUTED_LOUDSPEAKER

        if self._status_frame is None:
            self._status_frame = StatusFrame(p_window_title=self._window_title,
                                             p_size=self.get_window_size(),
                                             p_app_config=self._app_config, p_base_app=self)
            self._status_frame.init_buttons(p_time_extension_active=True, # todo
                                            p_label_format_string=ADD_MINUTE_LABEL_FORMAT_STRING)

        else:
            self.set_frame_size_and_title()

        self.set_time_extension_buttons()

        # See  https://stackoverflow.com/questions/5851932/changing-the-font-on-a-wxpython-textctrl-widget
        #self._status_font = wx.Font(self._app_config.status_message_font_size, wx.MODERN, wx.NORMAL, wx.NORMAL,
        #                            False, u'Consolas')
        #self._error_message_font = wx.Font(self._app_config.error_message_font_size,
        #                                   wx.MODERN, wx.NORMAL, wx.NORMAL, False, u'Consolas')

        self._color_warning_message = wx.Colour(self._app_config.color_warning_message)
        self._color_error_message = wx.Colour(self._app_config.color_error_message)
        self._color_normal_mode = wx.Colour(self._app_config.color_normal_mode)
        self._color_approaching_logout = wx.Colour(self._app_config.color_approaching_logout)

        self._color_warning_message_foreground = wx.Colour(self._app_config.color_warning_message_foreground)
        self._color_error_message_foreground = wx.Colour(self._app_config.color_error_message_foreground)
        self._color_normal_mode_foreground = wx.Colour(self._app_config.color_normal_mode_foreground)
        self._color_approaching_logout_foreground = wx.Colour(self._app_config.color_approaching_logout_foreground)

    def prepare_services(self, p_full_startup=True):

        config = self._config[audio_handler.SECTION_NAME]

        if self._arguments.speech_engine is not None:
            config.speech_engine = self._arguments.speech_engine

        if config.is_active():
            self._audio_handler = audio_handler.AudioHandler(p_config=config)
            self._audio_handler.init_engine()

        # Determine locale
        current_locale = None

        if self._arguments.locale is not None:
            current_locale = self._arguments.locale

        if current_locale is None:
            current_locale = self._app_config.locale

        if current_locale is None:
            (current_locale, _encoding) = locale.getdefaultlocale()

        locale_dir = os.path.join(os.path.dirname(__file__), "translations")

        self._locale_helper = locale_helper.LocaleHelper(p_locale_dir=locale_dir,
                                                         p_locale_selector=lambda: self._locale)

        self._ = self._locale_helper.gettext

        self.set_locale(p_locale=current_locale)

        # Determine username
        self._username = self._arguments.username

        if self._username is None:
            self._username = os.environ.get("USER")

        if self._username is None:
            raise configuration.ConfigurationException("No username set!")

        fmt = "Using username '{username}'"
        self._logger.info(fmt.format(username=self._username))

        status_connector_config = self._config[status_connector.SECTION_NAME]
        status_connector_config.host_url = self._arguments.server_url

        self._status_connector = status_connector.StatusConnector(p_config=status_connector_config, p_lang=self._)

        self.evaluate_configuration()

        self._icon = taskbar.TaskBarIcon(p_config=self._app_config, p_status_frame=self._status_frame,
                                         p_base_app=self, p_gettext=self._locale_helper.gettext,
                                         p_configuration_model=self._app_config)


        self.show_status_frame(self._app_config.show_window_upon_start)

        self.update_status()


        task = base_app.RecurringTask(p_name="app.updateStatus",
                                      p_handler_method=lambda: self.update_status(),
                                      p_interval=self._app_config.check_interval)
        self.add_recurring_task(p_recurring_task=task)

        self._taskbar_process = threading.Thread(target=self._wx_app.MainLoop)
        self._taskbar_process.start()

    def show_status_frame(self, p_show):
        wx.CallAfter(self._status_frame.Show, p_show)

    def stop_event_queue(self):

        if self._status_frame:
            self._status_frame.start_shutdown()

        self._icon = None
        super().stop_event_queue()

    def shutdown_gui(self):

        if self._status_frame is not None:
            self._status_frame.Destroy()
            self._status_frame = None

        if self._icon is not None:
            self._icon.shut_down()
            self._icon = None

    def stop_services(self):

        if self._status_frame:
            self._status_frame.start_shutdown()

        if self._taskbar_process is not None:
            if self._taskbar_process.is_alive():
                wx.Yield()
                wx.CallAfter(self.shutdown_gui)

            self._taskbar_process.join()
            self._taskbar_process = None

    def reevaluate_configuration(self):

        super().reevaluate_configuration()
        self.evaluate_configuration()
        self.update_status()

    def request_time_extension(self, p_button_index:int):
        self._status_connector.request_time_extension(
            p_username=self._username,
            p_secret=constants.DEFAULT_ACCESS_CODE,
            p_extension_length = self._app_config.add_time_intervals[p_button_index],
            )
        if self._user_status.ruleset_check_interval is not None:
            self._earliest_button_activation: datetime.datetime = \
                tools.get_current_time() + datetime.timedelta(seconds=self._user_status.ruleset_check_interval)

        self.set_time_extension_buttons()


def main():
    parser = get_argument_parser(p_app_name=configuration_model.APP_NAME)

    return base_app.main(p_app_name=configuration_model.APP_NAME, p_app_class=App, p_argument_parser=parser)


if __name__ == '__main__':
    exit(main())
