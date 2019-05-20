"""
Module docstring.
"""


class Abilities(object):
    """Class docstring."""

    STRENGTH = 'strength'
    DEXTERITY = 'dexterity'
    CONSTITUTION = 'constitution'
    INTELLIGENCE = 'intelligence'
    WISDOM = 'wisdom'
    CHARISMA = 'charisma'

    @classmethod
    def as_list(cls):
        """Method docstring."""
        return [
            cls.STRENGTH,
            cls.DEXTERITY,
            cls.CONSTITUTION,
            cls.INTELLIGENCE,
            cls.WISDOM,
            cls.CHARISMA
        ]
