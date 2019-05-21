"""
Module docstring.
"""


class Abilities(object):
    """Class docstring."""

    STRENGTH = 'Strength'
    DEXTERITY = 'Dexterity'
    CONSTITUTION = 'Constitution'
    INTELLIGENCE = 'Intelligence'
    WISDOM = 'Wisdom'
    CHARISMA = 'Charisma'

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

    @classmethod
    def iterate(cls):
        """Method docstring."""
        for skill in cls.as_list():
            yield skill
