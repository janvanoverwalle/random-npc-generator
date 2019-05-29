"""
Module docstring.
"""
import wx
from rng.models.characters import Character
from rng.resources.data.genders import Genders
from rng.resources.data.races import Races
from rng.resources.data.classes import Classes
from rng.resources.data.professions import Professions


class MainPanel(wx.Panel):
    """Class docstring."""

    LBL_HDR_TITLE = 'Click a button to generate a random character.'
    LBL_BTN_ROLL_NPC = 'Roll a random NPC'
    LBL_BTN_ROLL_PC = 'Roll a random PC'

    def __init__(self, parent):
        super().__init__(parent)
        self._parent = parent

        self.main_sizer = wx.BoxSizer(wx.VERTICAL)
        self.main_sizer.Add(self.create_header(), 0, wx.ALL | wx.CENTER, 5)
        self.main_sizer.Add(self.create_buttons(), 0, wx.ALL | wx.CENTER, 5)
        self.main_sizer.Add(self.create_options(), 0, wx.ALL | wx.EXPAND, 5)
        self.main_sizer.SetMinSize(parent.GetSize())
        self.SetSizer(self.main_sizer)
        self.Fit()

        print(self.gender_group.GetSize())

    def create_header(self):
        """Method docstring."""
        header_sizer = wx.BoxSizer(wx.VERTICAL)

        header = wx.StaticText(self)
        header.SetLabel(self.LBL_HDR_TITLE)
        header_sizer.Add(header, 0, wx.TOP | wx.CENTER, 5)

        return header_sizer

    def create_buttons(self):
        """Method docstring."""
        btn_width = int(max(len(self.LBL_BTN_ROLL_NPC), len(self.LBL_BTN_ROLL_PC))*7)

        btn_sizer = wx.BoxSizer(wx.HORIZONTAL)

        # NPC button
        roll_npc_btn = wx.Button(self, label=self.LBL_BTN_ROLL_NPC, size=(btn_width, -1))
        roll_npc_btn.Bind(wx.EVT_BUTTON, self._parent.on_click_roll_npc)
        btn_sizer.Add(roll_npc_btn, 0, wx.ALL | wx.CENTER, 5)

        btn_sizer.AddSpacer(20)

        # PC button
        roll_pc_btn = wx.Button(self, label=self.LBL_BTN_ROLL_PC, size=(btn_width, -1))
        roll_pc_btn.Bind(wx.EVT_BUTTON, self._parent.on_click_roll_pc)
        btn_sizer.Add(roll_pc_btn, 0, wx.ALL | wx.CENTER, 5)

        return btn_sizer

    def create_options(self):
        """Method docstring."""
        options_sizer = wx.BoxSizer(wx.VERTICAL)

        # Genders
        self.gender_group = self.create_checkbox_group(f'{Character.GENDER}s', Genders.as_list())
        options_sizer.Add(self.gender_group, 0, wx.RIGHT | wx.LEFT | wx.EXPAND, 25)
        # Races
        self.race_group = self.create_checkbox_group(f'{Character.RACE}s', Races.as_list())
        options_sizer.Add(self.race_group, 0, wx.RIGHT | wx.LEFT | wx.EXPAND, 25)
        # Class
        self.class_group = self.create_checkbox_group(f'{Character.CLASS}es', Classes.as_list())
        options_sizer.Add(self.class_group, 0, wx.RIGHT | wx.LEFT | wx.EXPAND, 25)
        # Professions
        prof_group_title = f'{Character.PROFESSION} Categories'
        self.prof_group = self.create_checkbox_group(prof_group_title, Professions.categories(), columns=4)
        options_sizer.Add(self.prof_group, 0, wx.RIGHT | wx.LEFT | wx.EXPAND, 25)

        return options_sizer

    def create_checkbox_group(self, title, options, columns=12):
        """Method docstring."""
        style_flags = wx.CP_DEFAULT_STYLE | wx.CP_NO_TLW_RESIZE
        pane_obj = wx.CollapsiblePane(self, label=title.title(), style=style_flags)
        pane_obj.Bind(wx.EVT_COLLAPSIBLEPANE_CHANGED, self.on_pane_state_change)
        pane = pane_obj.GetPane()

        checkbox_width = 0
        for option in options:
            checkbox_width = max(checkbox_width, len(option))
        print(checkbox_width)

        checkbox_sizer = wx.FlexGridSizer(cols=columns)
        checkbox_sizer.AddGrowableCol(columns-1)
        max_width = 0
        for option in options:
            checkbox = wx.CheckBox(pane, label=option)
            checkbox_sizer.Add(checkbox, 0, wx.EXPAND)
            max_width = max(max_width, checkbox.GetSize()[0])
        print(f'{title}: {max_width} ({max_width/checkbox_width})')

        border = wx.BoxSizer()
        border.Add(checkbox_sizer, 1, wx.EXPAND | wx.ALL, 5)

        pane.SetSizer(border)

        return pane_obj

    def on_pane_state_change(self, event=None):
        """Method docstring."""
        self.Layout()
