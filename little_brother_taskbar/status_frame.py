import os
import wx

from little_brother_taskbar.configuration_model import TaskBarAppConfigModel
from python_base_app.base_app import BaseApp


class StatusFrame(wx.Frame):

    def __init__(self, p_window_title:str, p_size:tuple, p_app_config:TaskBarAppConfigModel, p_base_app:BaseApp):

        super().__init__(parent=None, id=wx.ID_ANY, title=p_window_title,
                         size=p_size, style=wx.CAPTION | wx.STAY_ON_TOP | wx.RESIZE_BORDER)

        self._original_size = p_size
        self._app_config = p_app_config
        self._base_app = p_base_app

        self._static_text = None
        self._bit = 0
        self._in_shutdown = False

        self.Bind(wx.EVT_LEFT_UP, lambda x: self.Show(False))
        self.Bind(wx.EVT_CLOSE, lambda x: self.Show(False))

        self._static_text = wx.StaticText(self, id=wx.ID_ANY,
                                          style=wx.ALIGN_CENTER | wx.ALIGN_CENTER_VERTICAL)

        self._static_text.Bind(wx.EVT_LEFT_UP, lambda x: self.Show(False))
        self._static_text.Bind(wx.EVT_RIGHT_UP, self.on_toggle_notifications)


        icon = wx.NullIcon
        icon_path = os.path.join(os.path.dirname(__file__), "static/icons/little-brother-taskbar-logo_32x32.bmp")
        icon.CopyFromBitmap(wx.Bitmap(icon_path, wx.BITMAP_TYPE_BMP))
        self.SetIcon(icon)

    def on_toggle_notifications(self, _event):

        self._app_config.enable_spoken_notifications = not self._app_config.enable_spoken_notifications
        self._base_app.reevaluate_configuration()
        self._base_app.write_config_to_file()

    def update(self, p_size, p_window_title):

        self._original_size = p_size
        self.SetSize(p_size)
        self.SetTitle(p_window_title)

    def redraw_text(self, text, font, color, color_foreground):

        if not self._in_shutdown:
            self._static_text.SetFont(font)
            self.SetBackgroundColour(color)
            self._static_text.SetBackgroundColour(color)
            self._static_text.SetForegroundColour(color_foreground)
            self._static_text.SetLabel(text)
            self._static_text.Wrap(self.GetSize().GetWidth())

            # Ugly hack! to ensure that the content of the frame is updated. Refresh() or Update() do not help.
            self._bit ^= 1
            self.SetSize(size=(self._original_size[0], self._original_size[1] + self._bit))

    def start_shutdown(self):

        self._in_shutdown = True
