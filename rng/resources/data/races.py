"""
Module docstring.
"""


class Races(object):
    """Class docstring."""

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
    def as_list(cls):
        """Method docstring."""
        return [
            cls.DRAGONBORN,
            cls.HILL_DWARF,
            cls.MOUNTAIN_DWARF,
            cls.HIGH_ELF,
            cls.WOOD_ELF,
            cls.DARK_ELF,
            cls.ROCK_GNOME,
            cls.FOREST_GNOME,
            cls.HALF_ELF,
            cls.HALF_ORC,
            cls.LIGHTFOOT_HALFLING,
            cls.STOUT_HALFLING,
            cls.HUMAN,
            cls.TIEFLING,
        ]

    @classmethod
    def get_base_race(cls, race_name):
        """Method docstring."""
        return race_name.split(' ')[-1]
