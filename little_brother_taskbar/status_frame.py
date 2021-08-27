import os
import wx
import jinja2
from wx import Colour, C2S_HTML_SYNTAX, CommandEvent

from little_brother_taskbar import status_frame_wxglade, constants
from little_brother_taskbar.configuration_model import TaskBarAppConfigModel
from python_base_app.base_app import BaseApp
from little_brother_taskbar.button_info import ButtonInfo


class StatusFrame(status_frame_wxglade.StatusFrame):

    def __init__(self, p_window_title:str, p_size:tuple, p_app_config:TaskBarAppConfigModel, p_base_app:BaseApp):

        super().__init__(parent=None, id=wx.ID_ANY, size=p_size, style=wx.CAPTION | wx.STAY_ON_TOP)

        self._app_config = p_app_config
        self._app = p_base_app

        self._jinja2_env = jinja2.Environment(loader=jinja2.PackageLoader("little_brother_taskbar"))
        self._status_field_template = self._jinja2_env.get_template(constants.TEMPLATE_STATUS_FIELD)

        self._bit = 0
        self._in_shutdown = False
        self._add_time_buttons = []

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
        self._app.reevaluate_configuration()
        self._app.write_config_to_file()

    def update(self, p_size, p_window_title):

        self.SetSize(p_size)
        self.SetTitle(p_window_title)

    def init_buttons(self, p_time_extension_active:bool, p_label_format_string:str):

        self._label_format_string = p_label_format_string

        for sizer_item in self._sizer_buttons.Children:
            self._add_time_buttons.append(sizer_item.GetWindow())


    def set_buttons(self, p_time_extension_active, p_button_infos):

        self._sizer_buttons.ShowItems(p_time_extension_active)

        if p_time_extension_active:
            for i_button in range(0, len(self._add_time_buttons)):
                button:wx.Button = self._add_time_buttons[i_button]
                button_info:ButtonInfo = p_button_infos[i_button]

                button.Enable(button_info.active)
                button.SetLabelText(self._label_format_string.format(minutes=button_info.minutes))


    def button_request_time_extension_pressed(self, event:CommandEvent):

        i = 0

        for button in self._add_time_buttons:
            if button == event.EventObject:
                self._app.request_time_extension(p_button_index=i)

            i += 1

    def redraw_text(self, text:str, small_text:str, font_size:int, color:Colour,
                    color_foreground:Colour):

        if not self._in_shutdown:
            self.SetBackgroundColour(color)

            html_page = self._status_field_template.render(message=text.replace("\n", "<BR>"),
                                                           message2=small_text,
                                                           background_color=color.GetAsString(C2S_HTML_SYNTAX),
                                                           foreground_color=color_foreground.GetAsString(C2S_HTML_SYNTAX),
                                                           font_size=font_size,
                                                           small_font_site=int(font_size / 2))

            self._status_html_window.SetPage(html_page)


    def start_shutdown(self):

        self._in_shutdown = True
