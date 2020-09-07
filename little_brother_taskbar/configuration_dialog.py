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

import re

import wx

from little_brother_taskbar import configuration_dialog_wxglade
from little_brother_taskbar import configuration_model
from python_base_app import configuration
from python_base_app import log_handling

VALIDATION_PATTERN_INTEGER = "^ *[0-9]+ *$"

CONFIGURATION_DIALOG_RECTANGLE = (450, 650)
DEFAULT_BORDER = 5
DEFAULT_INVALID_FIELD_COLOR = "pink"

GRID_GAP_X = 5
GRID_GAP_Y = 5


# See https://stackoverflow.com/questions/2198903/wx-textctrl-and-wx-validator/3405979
class TextObjectValidator(wx.Validator):

    """ This validator is used to ensure that the user has entered something
        into the text object editor dialog's text field.
    """

    def __init__(self, p_pattern, p_error_message, p_gettext):

        """ Standard constructor."""

        wx.Validator.__init__(self)
        self._pattern = p_pattern
        self._error_message = p_error_message
        self._pattern_re = re.compile(p_pattern)
        self._ = p_gettext

    def Clone(self):

        """ Standard cloner.

            Note that every validator must implement the Clone() method.
        """
        return TextObjectValidator(self._pattern, self._error_message, self._)

    def Validate(self, win):
        """ Validate the contents of the given text control.
        """
        text_ctrl = self.GetWindow()
        text = text_ctrl.GetValue()

        match = self._pattern_re.match(text)

        if match is None:
            wx.MessageBox(self._error_message, self._("Error"), parent=text_ctrl)
            text_ctrl.SetBackgroundColour(DEFAULT_INVALID_FIELD_COLOR)
            text_ctrl.SetFocus()
            text_ctrl.Refresh()
            return False

        else:
            text_ctrl.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
            text_ctrl.Refresh()
            return True

    def TransferToWindow(self):

        """ Transfer data from validator to window.

            The default implementation returns False, indicating that an error
            occurred.  We simply return True, as we don't do any data transfer.
        """
        return True  # Prevent wxDialog from complaining.

    def TransferFromWindow(self):

        """ Transfer data from window to validator.

            The default implementation returns False, indicating that an error
            occurred.  We simply return True, as we don't do any data transfer.
        """
        return True  # Prevent wxDialog from complaining.


class ConfigurationDialog(configuration_dialog_wxglade.ConfigurationDialog):

    def __init__(self, *args, **kw):

        self._logger = log_handling.get_logger(self.__class__.__name__)

        super().__init__(*args, **kw)

        self.SetExtraStyle(wx.WS_EX_VALIDATE_RECURSIVELY)
        self._text_ctrl_check_interval.SetValidator(
            TextObjectValidator(p_pattern=VALIDATION_PATTERN_INTEGER, p_error_message=self._("Numeric value expected"),
                                p_gettext=self._))

        self.Center()

    def get_model(self, p_configuration_model: configuration_model.TaskBarAppConfigModel):

        try:
            p_configuration_model.check_interval = int(self._text_ctrl_check_interval.GetValue())
            p_configuration_model.warning_minutes_approaching_logout = \
                int(self._text_ctrl_warning_time_approaching_logout.GetValue())
            p_configuration_model.status_message_font_size = int(self._text_ctrl_status_message_font_size.GetValue())
            p_configuration_model.error_message_font_size = int(self._text_ctrl_error_message_font_size.GetValue())

            p_configuration_model.color_error_message = self._color_ctrl_error_message.GetColour().GetAsString()
            p_configuration_model.color_warning_message = self._color_ctrl_warning_message.GetColour().GetAsString()
            p_configuration_model.color_normal_mode = self._color_ctrl_normal_mode.GetColour().GetAsString()
            p_configuration_model.color_approaching_logout = \
                self._color_ctrl_approaching_logout.GetColour().GetAsString()
            p_configuration_model.color_error_message_foreground = \
                self._color_ctrl_error_message_foreground.GetColour().GetAsString()
            p_configuration_model.color_warning_message_foreground = \
                self._color_ctrl_warning_message_foreground.GetColour().GetAsString()
            p_configuration_model.color_normal_mode_foreground = \
                self._color_ctrl_normal_mode_foreground.GetColour().GetAsString()
            p_configuration_model.color_approaching_logout_foreground = \
                self._color_ctrl_approaching_logout_foreground.GetColour().GetAsString()

            p_configuration_model.window_height = int(self._text_ctrl_window_height.GetValue())
            p_configuration_model.window_width = int(self._text_ctrl_window_width.GetValue())

            p_configuration_model.show_window_upon_start = self._checkbox_show_window_upon_start.GetValue()
            p_configuration_model.show_window_when_approaching_logout = \
                self._checkbox_show_window_when_approaching_logout.GetValue()
            p_configuration_model.enable_spoken_notifications = self._checkbox_enable_spoken_notifications.GetValue()


        except Exception as e:
            fmt = self._("Exception '{exception}' while parsing options")
            msg = fmt.format(exception=str(e))
            self._logger.debug(msg)
            raise configuration.ConfigurationException(msg)

    def set_model(self, p_configuration_model: configuration_model.TaskBarAppConfigModel):

        self._text_ctrl_check_interval.SetValue(str(p_configuration_model.check_interval))
        self._text_ctrl_warning_time_approaching_logout.SetValue(
            str(p_configuration_model.warning_minutes_approaching_logout))

        self._text_ctrl_status_message_font_size.SetValue(str(p_configuration_model.status_message_font_size))
        self._text_ctrl_error_message_font_size.SetValue(str(p_configuration_model.error_message_font_size))

        self._color_ctrl_error_message.SetColour(wx.Colour(p_configuration_model.color_error_message))
        self._color_ctrl_warning_message.SetColour(wx.Colour(p_configuration_model.color_warning_message))
        self._color_ctrl_normal_mode.SetColour(wx.Colour(p_configuration_model.color_normal_mode))
        self._color_ctrl_approaching_logout.SetColour(wx.Colour(p_configuration_model.color_approaching_logout))
        self._color_ctrl_error_message_foreground.SetColour(
            wx.Colour(p_configuration_model.color_error_message_foreground))
        self._color_ctrl_warning_message_foreground.SetColour(
            wx.Colour(p_configuration_model.color_warning_message_foreground))
        self._color_ctrl_normal_mode_foreground.SetColour(
            wx.Colour(p_configuration_model.color_normal_mode_foreground))
        self._color_ctrl_approaching_logout_foreground.SetColour(
            wx.Colour(p_configuration_model.color_approaching_logout_foreground))

        self._text_ctrl_window_height.SetValue(str(p_configuration_model.window_height))
        self._text_ctrl_window_width.SetValue(str(p_configuration_model.window_width))

        self._checkbox_show_window_upon_start.SetValue(p_configuration_model.show_window_upon_start)
        self._checkbox_show_window_when_approaching_logout.SetValue(
            p_configuration_model.show_window_when_approaching_logout)
        self._checkbox_enable_spoken_notifications.SetValue(p_configuration_model.enable_spoken_notifications)
