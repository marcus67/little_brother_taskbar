import os
import wx
import jinja2
from wx import Colour, C2S_HTML_SYNTAX

from little_brother_taskbar import status_frame_wxglade, constants
from little_brother_taskbar.configuration_model import TaskBarAppConfigModel
from python_base_app.base_app import BaseApp


class StatusFrame(status_frame_wxglade.StatusFrame):

    def __init__(self, p_window_title:str, p_size:tuple, p_app_config:TaskBarAppConfigModel, p_base_app:BaseApp):

        super().__init__(parent=None, id=wx.ID_ANY, size=p_size, style=wx.CAPTION | wx.STAY_ON_TOP)

        self._app_config = p_app_config
        self._base_app = p_base_app

        self._jinja2_env = jinja2.Environment(loader=jinja2.PackageLoader("little_brother_taskbar"))
        self._status_field_template = self._jinja2_env.get_template(constants.TEMPLATE_STATUS_FIELD)

        self._bit = 0
        self._in_shutdown = False

        self.Bind(wx.EVT_LEFT_UP, lambda x: self.Show(False))
        self.Bind(wx.EVT_CLOSE, lambda x: self.Show(False))

        icon = wx.NullIcon
        icon_path = os.path.join(os.path.dirname(__file__), "static/icons/little-brother-taskbar-logo_32x32.bmp")
        icon.CopyFromBitmap(wx.Bitmap(icon_path, wx.BITMAP_TYPE_BMP))
        self.SetIcon(icon)
        self.SetTitle(p_window_title)
        self._status_html_window.SetSize(p_size)
        self.SetSize(p_size)

    def on_toggle_notifications(self, _event):

        self._app_config.enable_spoken_notifications = not self._app_config.enable_spoken_notifications
        self._base_app.reevaluate_configuration()
        self._base_app.write_config_to_file()

    def update(self, p_size, p_window_title):

        self.SetSize(p_size)
        self.SetTitle(p_window_title)

    def redraw_text(self, text:str, font_size:int, color:Colour, color_foreground:Colour):

        if not self._in_shutdown:
            self.SetBackgroundColour(color)

            html_page = self._status_field_template.render(message=text.replace("\n", "<BR>"),
                                                           background_color=color.GetAsString(C2S_HTML_SYNTAX),
                                                           foreground_color=color_foreground.GetAsString(C2S_HTML_SYNTAX),
                                                           font_size=font_size)

            self._status_html_window.SetPage(html_page)

            # Ugly hack! to ensure that the content of the frame is updated. Refresh() or Update() do not help.
            #self._bit ^= 1
            #self.SetSize(size=(self._original_size[0], self._original_size[1] + self._bit))

    def start_shutdown(self):

        self._in_shutdown = True
