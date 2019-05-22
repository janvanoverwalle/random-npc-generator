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
        for ability in cls.as_list():
            yield ability

    @classmethod
    def convert(cls, obj):
        """Method docstring."""
        if obj is None:
            return None
        parsed_string = ''.join([c for c in str(obj).lower() if c.isalpha()])
        for ability in cls.iterate():
            parsed_ability = ''.join([c for c in ability.lower() if c.isalpha()])
            if parsed_string == parsed_ability:
                return ability
        return str(obj)
