"""
Module docstring.
"""
import random
from rng.resources.data.genders import Genders


class CharacterGenders(object):
    """Class docstring."""

    @classmethod
    def roll_random(cls, amount=1):
        """Method docstring."""

        if not amount:
            return None

        results = [CharacterGender(s) for s in random.choices(Genders.as_list(), k=amount)]
        return results[0] if amount == 1 else results


class CharacterGender(object):
    """Class docstring."""

    def __init__(self, gender):
        self.gender = gender

    def __str__(self):
        return f'{self.gender}'

    @property
    def pronoun(self):
        """Method docstring."""
        if self.gender == Genders.MALE:
            return 'him'
        if self.gender == Genders.FEMALE:
            return 'her'
        return 'it'

