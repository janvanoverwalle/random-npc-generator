"""
Module docstring.
"""
from rng.resources.data.strings import Strings


class CharacterClasses(object):
    """Class docstring."""

    @classmethod
    def roll(cls, class_name=None, amount=1):
        """Method docstring."""
        if not amount:
            return None

        if not class_name or Strings.equals_ignore_case(class_name, Strings.RANDOM):
            results = [None]
        else:
            results = [None]
        return results[0] if amount == 1 else results

    @classmethod
    def roll_random(cls, amount=1):
        """Method docstring."""

        if not amount:
            return None

        return cls.roll(Strings.RANDOM, amount)
