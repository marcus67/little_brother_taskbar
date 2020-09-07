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

from python_base_app import base_app

APP_NAME = 'LittleBrotherTaskbar'
DEFAULT_UPDATE_INTERVAL = 5
DEFAULT_STATUS_FONT_SIZE = 24
DEFAULT_ERROR_MESSAGE_FONT_SIZE = 12
DEFAULT_SHOW_WINDOW_UPON_START = True
DEFAULT_SHOW_WINDOW_WHEN_APPROACHING_LOGOUT = True
DEFAULT_ENABLE_SPOKEN_NOTIFICATIONS = True
DEFAULT_COLOR_NORMAL_MODE = "rgb(138, 226, 52)"
DEFAULT_COLOR_APPROACHING_LOGOUT = "rgb(114, 159, 207)"
DEFAULT_COLOR_WARNING_MESSAGE = "rgb(252, 175, 62)"
DEFAULT_COLOR_ERROR_MESSAGE = "rgb(204, 0, 0)"
DEFAULT_COLOR_FOREGROUND = "rgb(0, 0, 0)"

DEFAULT_WARNING_MINUTES_APPROACHING_LOGOUT = 5
DEFAULT_WINDOW_WIDTH = 320
DEFAULT_WINDOW_HEIGHT = 110
DEFAULT_LOCALE = "en"

class TaskBarAppConfigModel(base_app.BaseAppConfigModel):

    def __init__(self):
        """Class for configuration of class `App`."""
        super().__init__(APP_NAME)

        self.check_interval = DEFAULT_UPDATE_INTERVAL
        self.status_message_font_size = DEFAULT_STATUS_FONT_SIZE
        self.error_message_font_size = DEFAULT_ERROR_MESSAGE_FONT_SIZE
        self.window_width = DEFAULT_WINDOW_WIDTH
        self.window_height = DEFAULT_WINDOW_HEIGHT
        self.show_window_upon_start = DEFAULT_SHOW_WINDOW_UPON_START
        self.show_window_when_approaching_logout = DEFAULT_SHOW_WINDOW_WHEN_APPROACHING_LOGOUT
        self.enable_spoken_notifications = DEFAULT_ENABLE_SPOKEN_NOTIFICATIONS
        self.color_normal_mode = DEFAULT_COLOR_NORMAL_MODE
        self.color_warning_message = DEFAULT_COLOR_WARNING_MESSAGE
        self.color_error_message = DEFAULT_COLOR_ERROR_MESSAGE
        self.color_approaching_logout = DEFAULT_COLOR_APPROACHING_LOGOUT
        self.color_normal_mode_foreground = DEFAULT_COLOR_FOREGROUND
        self.color_warning_message_foreground = DEFAULT_COLOR_FOREGROUND
        self.color_error_message_foreground = DEFAULT_COLOR_FOREGROUND
        self.color_approaching_logout_foreground = DEFAULT_COLOR_FOREGROUND
        self.warning_minutes_approaching_logout = DEFAULT_WARNING_MINUTES_APPROACHING_LOGOUT
        self.locale = DEFAULT_LOCALE
