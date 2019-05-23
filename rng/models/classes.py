"""
Module docstring.
"""
from rng.resources.data.strings import Strings


class CharacterClasses(object):
    """Class docstring."""

    @classmethod
    def roll(cls, class_name=None, amount=1):
        """Method docstring."""
        return []

    @classmethod
    def roll_random(cls, amount=1):
        """Method docstring."""

        if not amount:
            return None

        return cls.roll(Strings.RANDOM, amount)
