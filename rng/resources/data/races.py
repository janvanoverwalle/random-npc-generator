"""
Module docstring.
"""


class Races(object):
    """Class docstring."""

    KEY = 'race'

    DRAGONBORN = 'Dragonborn'
    DWARF = 'Dwarf'
    HILL_DWARF = f'Hill {DWARF}'
    MOUNTAIN_DWARF = f'Mountain {DWARF}'
    ELF = 'Elf'
    HIGH_ELF = f'High {ELF}'
    WOOD_ELF = f'Wood {ELF}'
    DARK_ELF = f'Dark {ELF}'
    GNOME = 'Gnome'
    ROCK_GNOME = f'Rock {GNOME}'
    FOREST_GNOME = f'Forest {GNOME}'
    HALF_ELF = 'Half-elf'
    HALF_ORC = 'Half-orc'
    HALFLING = 'Halfling'
    LIGHTFOOT_HALFLING = f'Lightfoot {HALFLING}'
    STOUT_HALFLING = f'Stout {HALFLING}'
    HUMAN = 'Human'
    TIEFLING = 'Tiefling'

    @classmethod
    def as_list(cls, subraces=None):
        """Method docstring."""
        ret = []
        ret.append(cls.DRAGONBORN)
        if not subraces:
            ret.append(cls.DWARF)
        else:
            ret.append(cls.HILL_DWARF)
            ret.append(cls.MOUNTAIN_DWARF)
        if not subraces:
            ret.append(cls.ELF)
        else:
            ret.append(cls.HIGH_ELF)
            ret.append(cls.WOOD_ELF)
            ret.append(cls.DARK_ELF)
        if not subraces:
            ret.append(cls.GNOME)
        else:
            ret.append(cls.ROCK_GNOME)
            ret.append(cls.FOREST_GNOME)
        ret.append(cls.HALF_ELF)
        ret.append(cls.HALF_ORC)
        if not subraces:
            ret.append(cls.HALFLING)
        else:
            ret.append(cls.LIGHTFOOT_HALFLING)
            ret.append(cls.STOUT_HALFLING)
        ret.append(cls.HUMAN)
        ret.append(cls.TIEFLING)
        return ret

    @classmethod
    def get_base_race(cls, race_name):
        """Method docstring."""
        return race_name.split(' ')[-1]

    @classmethod
    def is_valid(cls, obj):
        """Method docstring."""
        try:
            return obj.strip().lower() in cls.as_list()
        except Exception:
            return False

    @classmethod
    def to(cls, obj):
        """Method docstring."""
        try:
            for r in cls.as_list():
                if r.lower() == obj.lower():
                    return r
        except Exception:
            return obj
