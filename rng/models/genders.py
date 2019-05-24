"""
Module docstring.
"""
import random
from rng.resources.data.genders import Genders
from rng.resources.data.strings import Strings


class CharacterGenders(object):
    """Class docstring."""

    @classmethod
    def roll(cls, gender=None, amount=1):
        """Method docstring."""
        if not amount:
            return None

        if not gender or Strings.equals_ignore_case(gender, Strings.RANDOM):
            results = [CharacterGender(s) for s in random.choices(Genders.as_list(), k=amount)]
        else:
            results = [CharacterGender(gender)] * amount
        return results[0] if amount == 1 else results

    @classmethod
    def roll_random(cls, amount=1):
        """Method docstring."""
        return cls.roll(Strings.RANDOM, amount)


class CharacterGender(object):
    """Class docstring."""

    def __init__(self, gender):
        self.gender = gender

    def __str__(self):
        return f'{self.gender}'

    @property
    def object_pronoun(self):
        """Method docstring."""
        if self.gender == Genders.MALE:
            return 'him'
        if self.gender == Genders.FEMALE:
            return 'her'
        return 'it'

    @property
    def subject_pronoun(self):
        """Method docstring."""
        if self.gender == Genders.MALE:
            return 'he'
        if self.gender == Genders.FEMALE:
            return 'she'
        return 'it'

