#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 1.0.0a1 on Sun Aug 15 15:57:13 2021
#

import wx

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
from wx.html import HtmlWindow
# end wxGlade


class StatusFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: StatusFrame.__init__
        kwds["style"] = kwds.get("style", 0) | wx.CAPTION | wx.CLIP_CHILDREN | wx.CLOSE_BOX | wx.MAXIMIZE_BOX | wx.MINIMIZE_BOX | wx.SYSTEM_MENU
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((320, 180))
        self.SetTitle("TO BE SET")

        self.panel_status = wx.Panel(self, wx.ID_ANY)

        sizer_main = wx.BoxSizer(wx.VERTICAL)

        self._status_html_window = HtmlWindow(self.panel_status, wx.ID_ANY)
        self._status_html_window.SetMinSize((320, 140))
        sizer_main.Add(self._status_html_window, 5, wx.EXPAND | wx.FIXED_MINSIZE, 0)

        self._sizer_buttons = wx.BoxSizer(wx.HORIZONTAL)
        sizer_main.Add(self._sizer_buttons, 1, wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND | wx.SHAPED, 0)

        self._button_add_time_1 = wx.Button(self.panel_status, wx.ID_ANY, "min +1")
        self._button_add_time_1.SetMinSize((-1, 25))
        self._sizer_buttons.Add(self._button_add_time_1, 1, wx.EXPAND, 0)

        self._button_add_time_2 = wx.Button(self.panel_status, wx.ID_ANY, "min +2")
        self._button_add_time_2.SetMinSize((-1, 25))
        self._sizer_buttons.Add(self._button_add_time_2, 1, wx.EXPAND, 0)

        self._button_add_time_3 = wx.Button(self.panel_status, wx.ID_ANY, "min +3")
        self._button_add_time_3.SetMinSize((-1, 25))
        self._sizer_buttons.Add(self._button_add_time_3, 1, wx.EXPAND, 0)

        self.panel_status.SetSizer(sizer_main)

        self.Layout()

        self.Bind(wx.EVT_BUTTON, self.button_request_time_extension_pressed, self._button_add_time_1)
        self.Bind(wx.EVT_BUTTON, self.button_request_time_extension_pressed, self._button_add_time_2)
        self.Bind(wx.EVT_BUTTON, self.button_request_time_extension_pressed, self._button_add_time_3)
        # end wxGlade

    def button_request_time_extension_pressed(self, event):  # wxGlade: StatusFrame.<event_handler>
        print("Event handler 'button_request_time_extension_pressed' not implemented!")
        event.Skip()

# end of class StatusFrame

class MyApp(wx.App):
    def OnInit(self):
        self.frame = StatusFrame(None, wx.ID_ANY, "")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

# end of class MyApp

if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()
