"""
Module docstring.
"""
import wx
from rng.models.characters import Character


class CharacterPanel(wx.Panel):
    """Class docstring."""

    LBL_BTN_BACK = 'Back'

    def __init__(self, parent, character):
        super().__init__(parent)
        self.main_sizer = wx.BoxSizer(wx.VERTICAL)

        data_sizer = wx.BoxSizer(wx.VERTICAL)
        self.add_row_widget(Character.NAME, character.name, data_sizer)
        self.add_row_widget(Character.GENDER, character.gender, data_sizer)
        self.add_row_widget(Character.RACE, character.race, data_sizer)
        if character.has_class():
            self.add_row_widget(Character.CLASS, character.cclass, data_sizer)
        else:
            self.add_row_widget(Character.PROFESSION, character.profession, data_sizer)
        self.main_sizer.Add(data_sizer, 1, wx.EXPAND)

        btn_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.back_btn = wx.Button(self, label=self.LBL_BTN_BACK)
        self.back_btn.Bind(wx.EVT_BUTTON, parent.on_click_back)
        btn_sizer.Add(self.back_btn, 0, wx.ALL)
        self.main_sizer.Add(btn_sizer, 0, wx.ALL | wx.ALIGN_RIGHT, 5)

        self.main_sizer.SetMinSize(parent.GetSize())
        self.SetSizer(self.main_sizer)
        self.Fit()

    def add_row_widget(self, label, text, sizer=None):
        """Method docstring."""
        row_sizer = wx.BoxSizer(wx.HORIZONTAL)
        static_text = wx.StaticText(self, label=f'{label.title()}:', size=(60, -1))
        #static_text.SetLabel(f'{label.capitalize()}:')
        row_sizer.Add(static_text, 0, wx.ALL, 5)
        text_ctrl = wx.TextCtrl(self, value=f'{text}')
        row_sizer.Add(text_ctrl, 1, wx.ALL | wx.EXPAND, 5)

        sizer = sizer if sizer else self.main_sizer
        sizer.Add(row_sizer, 0, wx.EXPAND)
