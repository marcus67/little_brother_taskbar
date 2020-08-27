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

import os.path

import wx
import wx.adv

from little_brother_taskbar import configuration_dialog

TRAY_TOOLTIP = 'LittleBrother Tray'
TRAY_ICON = os.path.join(os.path.dirname(__file__), 'static/icons/little-brother-taskbar-logo_32x32.png')


def create_menu_item(menu, label, func):
    item = wx.MenuItem(menu, -1, label)
    menu.Bind(wx.EVT_MENU, func, id=item.GetId())
    menu.Append(item)
    return item


class TaskBarIcon(wx.adv.TaskBarIcon):
    def __init__(self, p_config, p_status_frame, p_base_app, p_gettext, p_configuration_model):
        """Entity to implement a taskbar tray icon for the application."""
        super(TaskBarIcon, self).__init__()
        self._config = p_config
        self._status_frame = p_status_frame
        self._base_app = p_base_app
        self._ = p_gettext
        self._configuration_model = p_configuration_model
        self.set_icon(TRAY_ICON)
        self.Bind(wx.adv.EVT_TASKBAR_LEFT_DOWN, self.on_left_down)

    def CreatePopupMenu(self):
        menu = wx.Menu()
        create_menu_item(menu, self._('Configuration'), self.on_configuration)
        create_menu_item(menu, self._('Exit'), self.on_exit)
        return menu

    def set_icon(self, path):
        icon = wx.Icon()
        icon.CopyFromBitmap(wx.Bitmap(path))
        self.SetIcon(icon, TRAY_TOOLTIP)

    def on_left_down(self, _event):
        self._status_frame.Show(not self._status_frame.IsShown())

    def on_exit(self, _event):
        self.shut_down()

    def on_configuration(self, _event):

        with configuration_dialog.ConfigurationDialog(None, p_gettext=self._) as dialog:
            dialog.set_model(p_configuration_model=self._configuration_model)

            if dialog.ShowModal() == wx.ID_OK:
                try:
                    dialog.get_model(p_configuration_model=self._configuration_model)
                    self._base_app.reevaluate_configuration()
                    self._base_app.write_config_to_file()

                except Exception as e:
                    wx.MessageDialog(dialog, str(e), caption=self._("Invalid Input"),
                                     style=wx.CENTRE|wx.OK_DEFAULT, pos=wx.DefaultPosition).ShowModal()


    def shut_down(self):
        wx.CallAfter(self.Destroy)
        self._status_frame.Close()
        self._base_app.stop_event_queue()
