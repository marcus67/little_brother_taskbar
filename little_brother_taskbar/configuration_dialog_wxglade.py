# -*- coding: UTF-8 -*-
#
# generated by wxGlade 1.0.0a1 on Mon Aug 16 23:28:13 2021
#

import wx

# begin wxGlade: dependencies
import gettext
# end wxGlade

# begin wxGlade: extracode
# Copyright (C) 2019  Marcus Rickert
#
# See https://github.com/marcus67/little_brother_taskbar
# end wxGlade


class ConfigurationDialog(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: ConfigurationDialog.__init__
        self._ = kwds.get("p_gettext", lambda x:x)
        del(kwds["p_gettext"])
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_DIALOG_STYLE
        wx.Dialog.__init__(self, *args, **kwds)
        self.SetTitle(self._("LittleBrotherTaskbar Configuration"))

        sizer_dialog = wx.BoxSizer(wx.VERTICAL)

        self.notebook = wx.Notebook(self, wx.ID_ANY)
        sizer_dialog.Add(self.notebook, 6, wx.EXPAND, 0)

        self.Timings = wx.Panel(self.notebook, wx.ID_ANY)
        self.notebook.AddPage(self.Timings, self._("Timings"))

        sizer_timings = wx.StaticBoxSizer(wx.StaticBox(self.Timings, wx.ID_ANY, ""), wx.VERTICAL)

        grid_sizer_timings = wx.FlexGridSizer(3, 2, 5, 5)
        sizer_timings.Add(grid_sizer_timings, 1, wx.ALL, 5)

        label_text_ctrl_check_interval = wx.StaticText(self.Timings, wx.ID_ANY, self._("Check Interval [seconds]"))
        grid_sizer_timings.Add(label_text_ctrl_check_interval, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self._text_ctrl_check_interval = wx.TextCtrl(self.Timings, wx.ID_ANY, "")
        self._text_ctrl_check_interval.SetToolTip(self._("Set the time in seconds between two status checks of LittleBrother."))
        grid_sizer_timings.Add(self._text_ctrl_check_interval, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        label_text_ctrl_warning_time_approaching_logout = wx.StaticText(self.Timings, wx.ID_ANY, self._("Warning Time Before Logout [minutes]"))
        grid_sizer_timings.Add(label_text_ctrl_warning_time_approaching_logout, 0, wx.ALL, 5)

        self._text_ctrl_warning_time_approaching_logout = wx.TextCtrl(self.Timings, wx.ID_ANY, "")
        self._text_ctrl_warning_time_approaching_logout.SetToolTip(self._("Set the time in minutes before logout when notifications will start appearing."))
        grid_sizer_timings.Add(self._text_ctrl_warning_time_approaching_logout, 0, wx.ALL, 5)

        label_text_ctrl_add_time_intervals = wx.StaticText(self.Timings, wx.ID_ANY, self._("Time Extension Intervals [minutes]"))
        grid_sizer_timings.Add(label_text_ctrl_add_time_intervals, 0, wx.ALL, 5)

        self._text_ctrl_add_time_intervals = wx.TextCtrl(self.Timings, wx.ID_ANY, "")
        grid_sizer_timings.Add(self._text_ctrl_add_time_intervals, 0, wx.ALL, 5)

        self.Colors = wx.Panel(self.notebook, wx.ID_ANY)
        self.notebook.AddPage(self.Colors, self._("Colors"))

        sizer_background_colors = wx.StaticBoxSizer(wx.StaticBox(self.Colors, wx.ID_ANY, ""), wx.VERTICAL)

        grid_sizer_background_colors = wx.FlexGridSizer(5, 3, 5, 5)
        sizer_background_colors.Add(grid_sizer_background_colors, 1, wx.ALL | wx.EXPAND, 5)

        label_empty_1 = wx.StaticText(self.Colors, wx.ID_ANY, "")
        grid_sizer_background_colors.Add(label_empty_1, 0, wx.ALL, 5)

        label_foreground = wx.StaticText(self.Colors, wx.ID_ANY, self._("Foreground"))
        grid_sizer_background_colors.Add(label_foreground, 0, wx.ALL, 5)

        label_background = wx.StaticText(self.Colors, wx.ID_ANY, self._("Background"))
        grid_sizer_background_colors.Add(label_background, 0, wx.ALL, 5)

        label_color_ctrl_error_message = wx.StaticText(self.Colors, wx.ID_ANY, self._("Error Message"))
        grid_sizer_background_colors.Add(label_color_ctrl_error_message, 0, wx.ALL, 5)

        self._color_ctrl_error_message_foreground = wx.ColourPickerCtrl(self.Colors, wx.ID_ANY)
        grid_sizer_background_colors.Add(self._color_ctrl_error_message_foreground, 0, wx.ALL | wx.EXPAND, 5)

        self._color_ctrl_error_message = wx.ColourPickerCtrl(self.Colors, wx.ID_ANY)
        grid_sizer_background_colors.Add(self._color_ctrl_error_message, 0, wx.ALL | wx.EXPAND, 5)

        label_color_ctrl_warning_message = wx.StaticText(self.Colors, wx.ID_ANY, self._("Warning Message"))
        grid_sizer_background_colors.Add(label_color_ctrl_warning_message, 0, wx.ALL, 5)

        self._color_ctrl_warning_message_foreground = wx.ColourPickerCtrl(self.Colors, wx.ID_ANY)
        grid_sizer_background_colors.Add(self._color_ctrl_warning_message_foreground, 0, wx.ALL | wx.EXPAND, 5)

        self._color_ctrl_warning_message = wx.ColourPickerCtrl(self.Colors, wx.ID_ANY)
        grid_sizer_background_colors.Add(self._color_ctrl_warning_message, 0, wx.ALL | wx.EXPAND, 5)

        label_color_ctrl_normal_mode = wx.StaticText(self.Colors, wx.ID_ANY, self._("Normal Mode"))
        grid_sizer_background_colors.Add(label_color_ctrl_normal_mode, 0, wx.ALL, 5)

        self._color_ctrl_normal_mode_foreground = wx.ColourPickerCtrl(self.Colors, wx.ID_ANY)
        grid_sizer_background_colors.Add(self._color_ctrl_normal_mode_foreground, 0, wx.ALL | wx.EXPAND, 5)

        self._color_ctrl_normal_mode = wx.ColourPickerCtrl(self.Colors, wx.ID_ANY)
        grid_sizer_background_colors.Add(self._color_ctrl_normal_mode, 0, wx.ALL | wx.EXPAND, 5)

        label_color_ctrl_approaching_logout = wx.StaticText(self.Colors, wx.ID_ANY, self._("Approaching Logout"))
        grid_sizer_background_colors.Add(label_color_ctrl_approaching_logout, 0, wx.ALL, 5)

        self._color_ctrl_approaching_logout_foreground = wx.ColourPickerCtrl(self.Colors, wx.ID_ANY)
        grid_sizer_background_colors.Add(self._color_ctrl_approaching_logout_foreground, 0, wx.ALL | wx.EXPAND, 5)

        self._color_ctrl_approaching_logout = wx.ColourPickerCtrl(self.Colors, wx.ID_ANY)
        grid_sizer_background_colors.Add(self._color_ctrl_approaching_logout, 0, wx.ALL | wx.EXPAND, 5)

        self.Sizes = wx.Panel(self.notebook, wx.ID_ANY)
        self.notebook.AddPage(self.Sizes, self._("Sizes"))

        sizer_1 = wx.BoxSizer(wx.VERTICAL)

        sizer_font_sizes = wx.StaticBoxSizer(wx.StaticBox(self.Sizes, wx.ID_ANY, self._("Font")), wx.VERTICAL)
        sizer_1.Add(sizer_font_sizes, 3, wx.ALL | wx.EXPAND, 5)

        grid_sizer_font_sizes = wx.FlexGridSizer(2, 2, 5, 5)
        sizer_font_sizes.Add(grid_sizer_font_sizes, 1, wx.EXPAND, 0)

        label_text_ctrl_status_message_font_size = wx.StaticText(self.Sizes, wx.ID_ANY, self._("Status Messages [pixel]"))
        grid_sizer_font_sizes.Add(label_text_ctrl_status_message_font_size, 0, wx.ALL, 5)

        self._text_ctrl_status_message_font_size = wx.TextCtrl(self.Sizes, wx.ID_ANY, "")
        grid_sizer_font_sizes.Add(self._text_ctrl_status_message_font_size, 0, wx.ALL, 5)

        label_text_ctrl_error_message_font_size = wx.StaticText(self.Sizes, wx.ID_ANY, self._("Error Messages [pixel]"))
        grid_sizer_font_sizes.Add(label_text_ctrl_error_message_font_size, 0, wx.ALL, 5)

        self._text_ctrl_error_message_font_size = wx.TextCtrl(self.Sizes, wx.ID_ANY, "")
        grid_sizer_font_sizes.Add(self._text_ctrl_error_message_font_size, 0, wx.ALL, 5)

        sizer_window_size = wx.StaticBoxSizer(wx.StaticBox(self.Sizes, wx.ID_ANY, self._("Window")), wx.VERTICAL)
        sizer_1.Add(sizer_window_size, 3, wx.ALL | wx.EXPAND, 5)

        grid_sizer_window_size = wx.FlexGridSizer(2, 2, 5, 5)
        sizer_window_size.Add(grid_sizer_window_size, 1, wx.ALL, 5)

        label_text_ctrl_window_width = wx.StaticText(self.Sizes, wx.ID_ANY, self._("Width [pixel]"))
        grid_sizer_window_size.Add(label_text_ctrl_window_width, 0, wx.ALL, 5)

        self._text_ctrl_window_width = wx.TextCtrl(self.Sizes, wx.ID_ANY, "")
        grid_sizer_window_size.Add(self._text_ctrl_window_width, 0, wx.ALL, 5)

        label_text_ctrl_window_height = wx.StaticText(self.Sizes, wx.ID_ANY, self._("Height [pixel]"))
        grid_sizer_window_size.Add(label_text_ctrl_window_height, 0, wx.ALL, 5)

        self._text_ctrl_window_height = wx.TextCtrl(self.Sizes, wx.ID_ANY, "")
        grid_sizer_window_size.Add(self._text_ctrl_window_height, 0, wx.ALL, 5)

        self.Behavior = wx.Panel(self.notebook, wx.ID_ANY)
        self.notebook.AddPage(self.Behavior, self._("Behavior"))

        sizer_behavior = wx.StaticBoxSizer(wx.StaticBox(self.Behavior, wx.ID_ANY, ""), wx.VERTICAL)

        grid_sizer_behavior = wx.FlexGridSizer(3, 2, 5, 5)
        sizer_behavior.Add(grid_sizer_behavior, 1, wx.ALL | wx.EXPAND, 5)

        label_enable_spoken_notifications = wx.StaticText(self.Behavior, wx.ID_ANY, self._("Enable Spoken Notifications"))
        grid_sizer_behavior.Add(label_enable_spoken_notifications, 0, wx.ALL, 5)

        self._checkbox_enable_spoken_notifications = wx.CheckBox(self.Behavior, wx.ID_ANY, "")
        grid_sizer_behavior.Add(self._checkbox_enable_spoken_notifications, 0, wx.ALL, 5)

        label_checkbox_show_window_upon_start = wx.StaticText(self.Behavior, wx.ID_ANY, self._("Show Window Upon Start"))
        grid_sizer_behavior.Add(label_checkbox_show_window_upon_start, 0, wx.ALL, 5)

        self._checkbox_show_window_upon_start = wx.CheckBox(self.Behavior, wx.ID_ANY, "")
        grid_sizer_behavior.Add(self._checkbox_show_window_upon_start, 0, wx.ALL, 5)

        label_checkbox_show_window_when_approaching_logout = wx.StaticText(self.Behavior, wx.ID_ANY, self._("Show Window When Approaching Logout"))
        grid_sizer_behavior.Add(label_checkbox_show_window_when_approaching_logout, 0, wx.ALL, 5)

        self._checkbox_show_window_when_approaching_logout = wx.CheckBox(self.Behavior, wx.ID_ANY, "")
        grid_sizer_behavior.Add(self._checkbox_show_window_when_approaching_logout, 0, wx.ALL, 5)

        sizer_buttons = wx.StdDialogButtonSizer()
        sizer_dialog.Add(sizer_buttons, 1, wx.ALIGN_RIGHT | wx.ALL, 5)

        self._cancel_button = wx.Button(self, wx.ID_CANCEL, self._("Cancel"))
        sizer_buttons.Add(self._cancel_button, 0, 0, 0)

        self._ok_button = wx.Button(self, wx.ID_OK, self._("OK"))
        self._ok_button.SetDefault()
        sizer_buttons.Add(self._ok_button, 0, 0, 0)

        sizer_buttons.Realize()

        self.Behavior.SetSizer(sizer_behavior)

        self.Sizes.SetSizer(sizer_1)

        self.Colors.SetSizer(sizer_background_colors)

        self.Timings.SetSizer(sizer_timings)

        self.SetSizer(sizer_dialog)
        sizer_dialog.Fit(self)

        self.Layout()
        # end wxGlade

# end of class ConfigurationDialog
