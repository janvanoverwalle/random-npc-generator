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
    LBL_CHKBX_ENABLE = 'Enable'
    LBL_CHKBX_DISABLE = 'Disable'

    def __init__(self, parent):
        super().__init__(parent)
        self._parent = parent

        self.visible_options = set()
        self.state_checkboxes = {}
        self.option_containers = {}
        self.options_sizer = None
        self.options_created = set()

        self.main_sizer = wx.BoxSizer(wx.VERTICAL)
        self.main_sizer.Add(self.create_header(), 0, wx.ALL | wx.CENTER, 5)
        self.main_sizer.Add(self.create_buttons(), 0, wx.ALL | wx.CENTER, 5)
        self.main_sizer.Add(self.create_options(), 0, wx.ALL | wx.CENTER, 5)
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
        if not self.options_sizer:
            self.options_sizer = wx.BoxSizer(wx.HORIZONTAL)

        # Genders
        gender_options = Genders.as_list() if Character.GENDER in self.visible_options else None
        self.gender_group = self.create_checkbox_group(Character.GENDER, gender_options)
        if 'gender' not in self.options_created:
            self.options_created.add('gender')
            self.options_sizer.Add(self.gender_group, 0, wx.RIGHT | wx.LEFT, 25)

        # Races
        # race_options = Races.as_list() if Character.RACE in self.visible_options else None
        # self.race_group = self.create_checkbox_group(Character.RACE, race_options)
        # self.options_sizer.Add(self.race_group, 0, wx.RIGHT | wx.LEFT, 25)

        # Class
        # class_options = Classes.as_list() if Character.CLASS in self.visible_options else None
        # self.class_group = self.create_checkbox_group(Character.CLASS, class_options)
        # self.options_sizer.Add(self.class_group, 0, wx.RIGHT | wx.LEFT, 25)

        # Professions
        # prof_options = Professions.categories() if Character.PROFESSION in self.visible_options else None
        # self.prof_group = self.create_checkbox_group(Character.PROFESSION, prof_options)
        # self.options_sizer.Add(self.prof_group, 0, wx.RIGHT | wx.LEFT, 25)

        return self.options_sizer

    def create_checkbox_group(self, title, options=None):
        """Method docstring."""
        root_container = self.option_containers.get(title, wx.BoxSizer(wx.VERTICAL))
        root_container.Clear()

        static_box = wx.StaticBox(self, -1, title.title())
        static_box_sizer = wx.StaticBoxSizer(static_box, orient=wx.VERTICAL)

        state_checkbox = self.state_checkboxes.get(title)
        if not state_checkbox:
            state_checkbox = wx.CheckBox(self, label=self.LBL_CHKBX_ENABLE)
            self.state_checkboxes[title] = state_checkbox
            state_checkbox.Bind(wx.EVT_CHECKBOX, lambda e: self.on_option_group_change(e, title))

        root_container.Add(state_checkbox, 0, wx.ALL | wx.EXPAND, 5)

        options_container = wx.BoxSizer(wx.VERTICAL)

        if options:
            for option in options:
                checkbox = wx.CheckBox(self, label=option.replace('&', '&&'))
                options_container.Add(checkbox, 0, wx.EXPAND | wx.TOP | wx.BOTTOM, 2)

        static_box_sizer.Add(options_container, 0, wx.ALL, 5)
        root_container.Add(static_box_sizer)
        self.option_containers[title] = root_container
        return root_container

    def on_option_group_change(self, event, data=None):
        """Method docstring."""
        if event.IsChecked():
            if data not in self.visible_options:
                self.visible_options.add(data)
        else:
            if data in self.visible_options:
                self.visible_options.remove(data)
        if data in self.option_containers:
            self.option_containers[data].Clear(True)
        self.create_options()
        self.Layout()
