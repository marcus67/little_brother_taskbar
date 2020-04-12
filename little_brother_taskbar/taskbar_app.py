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

import gettext
import locale
import os.path
import threading

import wx
import wx.adv

from little_brother_taskbar import status_connector
from little_brother_taskbar import taskbar
from python_base_app import base_app
from python_base_app import configuration
from python_base_app import audio_handler

APP_NAME = 'LittleBrotherTaskbar'
DEFAULT_UPDATE_INTERVAL = 5
DEFAULT_STATUS_FONT_SIZE = 24
DEFAULT_ERROR_MESSAGE_FONT_SIZE = 12
DEFAULT_SHOW_ON_START = True
DEFAULT_COLOR_NORMAL_MODE = "lightgreen"
DEFAULT_COLOR_APPROACHING_LOGOUT = "red"
DEFAULT_COLOR_WARNING = "yellow"
DEFAULT_COLOR_ERROR = "red"
DEFAULT_MINUTES_APPROACHING_LOGOUT = 5
DEFAULT_WINDOW_WIDTH = 320
DEFAULT_WINDOW_HEIGHT = 110
DEFAULT_LOCALE = "en_US"


# Dummy function to trigger extraction by pybabel...
# _ = lambda x, y=None: x


class TaskBarAppConfigModel(base_app.BaseAppConfigModel):

    def __init__(self):
        """Class for configuration of class `App`."""
        super().__init__(APP_NAME)

        self.check_interval = DEFAULT_UPDATE_INTERVAL
        self.status_font_size = DEFAULT_STATUS_FONT_SIZE
        self.error_message_font_size = DEFAULT_ERROR_MESSAGE_FONT_SIZE
        self.window_width = DEFAULT_WINDOW_WIDTH
        self.window_height = DEFAULT_WINDOW_HEIGHT
        self.show_on_start = DEFAULT_SHOW_ON_START
        self.color_normal_mode = DEFAULT_COLOR_NORMAL_MODE
        self.color_warning = DEFAULT_COLOR_WARNING
        self.color_error = DEFAULT_COLOR_ERROR
        self.color_approaching_logout = DEFAULT_COLOR_APPROACHING_LOGOUT
        self.minutes_approaching_logout = DEFAULT_MINUTES_APPROACHING_LOGOUT
        self.locale = DEFAULT_LOCALE


def get_argument_parser(p_app_name):
    parser = base_app.get_argument_parser(p_app_name=p_app_name)
    parser.add_argument('--server-url', dest='server_url', action='store',
                        help='Set the URL to retrieve user status')
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
        self._app_config = None
        self._status_frame = None
        self._status_connector = None
        self._audio_handler = None
        self._tasktar_process = None
        self._username = None
        self._latest_notification = None
        self._locale = None

        self.check_user_configuration_file()

    def load_configuration(self, p_configuration):

        status_connector_section = status_connector.StatusConnectorConfigModel()
        p_configuration.add_section(status_connector_section)

        audio_handler_section = audio_handler.AudioHandlerConfigModel()
        audio_handler_section.spool_dir = "/tmp"
        p_configuration.add_section(audio_handler_section)

        self._app_config = TaskBarAppConfigModel()
        p_configuration.add_section(self._app_config)

        return super(App, self).load_configuration(p_configuration=p_configuration)

    def set_locale(self, p_locale):

        if self._locale is None or p_locale != self._locale:
            localedir = os.path.join(os.path.dirname(__file__), "translations")
            self._lang = gettext.translation("messages", localedir=localedir,
                                             languages=[p_locale], fallback=True)
            if self._locale is None:
                fmt = "Using locale '{locale}'"

            else:
                fmt = "Switching to locale '{locale}'"

            self._logger.info(fmt.format(locale=p_locale))
            self._ = self._lang.gettext
            self._locale = p_locale

    def speak_status(self, p_user_status):

        if self._audio_handler is not None:
            if p_user_status.notification is not None and p_user_status.notification != self._latest_notification:
                self._audio_handler.notify(p_text=p_user_status.notification, p_locale=p_user_status.locale)
                self._latest_notification = p_user_status.notification


    def update_status(self):
        self._logger.debug("update_status")

        user_status = self._status_connector.request_status(p_username=self._username)

        if user_status is not None:

            if isinstance(user_status, str):
                font = self._error_message_font
                color = self._app_config.color_error
                text = user_status

            else:

                self.set_locale(p_locale=user_status.locale)
                self.speak_status(p_user_status=user_status)

                font = self._status_font

                if not user_status.logged_in:
                    color = self._app_config.color_warning
                    font = self._error_message_font
                    fmt = self._("User '{username}' not logged in")
                    text = fmt.format(username=self._username)

                elif user_status.activity_allowed:
                    if user_status.minutes_left_in_session is not None:
                        fmt = self._("Time left:\n{minutes} minutes")
                        text = fmt.format(minutes=user_status.minutes_left_in_session)

                        if user_status.minutes_left_in_session <= self._app_config.minutes_approaching_logout:
                            color = self._app_config.color_approaching_logout

                        else:
                            color = self._app_config.color_normal_mode

                    else:
                        text = self._("Unlimited Time")
                        color = self._app_config.color_normal_mode

                else:
                    color = self._app_config.color_warning
                    text = self._("No Activity Allowed")

            # https://stackoverflow.com/questions/14320836/wxpython-pango-error-when-using-a-while-true-loop-in-a-thread
            wx.CallAfter(self._static_text.SetFont, font)
            wx.CallAfter(self._status_frame.SetBackgroundColour, wx.Colour(color))
            wx.CallAfter(self._static_text.SetBackgroundColour, wx.Colour(color))
            wx.CallAfter(self._static_text.SetLabel, text)
            wx.CallAfter(self._static_text.Wrap, self._app_config.window_width)

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

        task = base_app.RecurringTask(p_name="app.updateStatus",
                                      p_handler_method=lambda: self.update_status(),
                                      p_interval=self._app_config.check_interval)
        self.add_recurring_task(p_recurring_task=task)

        self._status_frame = wx.Frame(None, id=wx.ID_ANY, title=APP_NAME,
                                      style=wx.CAPTION | wx.STAY_ON_TOP | wx.RESIZE_BORDER,
                                      size=(self._app_config.window_width, self._app_config.window_height))

        self._static_text = wx.StaticText(self._status_frame, id=wx.ID_ANY,
                                          style=wx.ALIGN_CENTER | wx.ALIGN_CENTER_VERTICAL)

        # See  https://stackoverflow.com/questions/5851932/changing-the-font-on-a-wxpython-textctrl-widget
        self._status_font = wx.Font(self._app_config.status_font_size, wx.MODERN, wx.NORMAL, wx.NORMAL,
                                    False, u'Consolas')
        self._error_message_font = wx.Font(self._app_config.error_message_font_size,
                                           wx.MODERN, wx.NORMAL, wx.NORMAL, False, u'Consolas')

        self.update_status()
        self._status_frame.Show(self._app_config.show_on_start)

        self._icon = taskbar.TaskBarIcon(p_config=self._app_config, p_status_frame=self._status_frame,
                                         p_base_app=self)

        self._taskbar_process = threading.Thread(target=self._wx_app.MainLoop)
        self._taskbar_process.start()

    def stop_event_queue(self):
        self._icon = None
        super().stop_event_queue()

    def stop_services(self):

        if self._taskbar_process is not None:
            if self._taskbar_process.is_alive() and self._icon is not None:
                wx.CallAfter(self._icon.shut_down)

            self._taskbar_process.join()
            self._taskbar_process = None


def main():
    parser = get_argument_parser(p_app_name=APP_NAME)

    return base_app.main(p_app_name=APP_NAME, p_app_class=App, p_argument_parser=parser)


if __name__ == '__main__':
    exit(main())
