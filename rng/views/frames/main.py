"""
Module docstring.
"""
import wx
from rng.views.panels.main import MainPanel
from rng.views.panels.character import CharacterPanel
from rng.models.characters import Characters

class MainFrame(wx.Frame):
    """Class docstring."""

    TITLE = 'Random NPC Generator'

    def __init__(self, width=None):
        width = width if width else 960
        super().__init__(parent=None, title=self.TITLE, size=(width, (width//16)*9))
        self.SetMinSize(self.GetSize())
        self.main_sizer = wx.BoxSizer(wx.VERTICAL)
        self.add_panel(MainPanel)
        self.Center()
        self.Show()

    def add_panel(self, panel, *args, **kwargs):
        """Method docstring."""
        try:
            if self.panel:
                self.panel.Destroy()
        except AttributeError:
            pass
        self.panel = panel(self, *args, **kwargs)
        self.main_sizer.Add(self.panel, -1, flag=wx.EXPAND)
        self.SetSizer(self.main_sizer)
        self.Layout()

    def on_click_roll_npc(self, event=None):
        """Method docstring."""
        npc = Characters.roll_npc()
        self.add_panel(CharacterPanel, npc)

    def on_click_roll_pc(self, event=None):
        """Method docstring."""
        pc = Characters.roll_pc()
        self.add_panel(CharacterPanel, pc)

    def on_click_back(self, event=None):
        """Method docstring."""
        _id = event.GetEventObject().Id
        try:
            if self.panel.back_btn.Id == _id:
                self.add_panel(MainPanel)
        except AttributeError:
            pass
