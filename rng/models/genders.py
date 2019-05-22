"""
Module docstring.
"""
import random


class CharacterGenders(object):
    """Class docstring."""

    MALE = 'Male'
    FEMALE = 'Female'

    @classmethod
    def as_list(cls):
        """Method docstring."""
        return [
            cls.MALE,
            cls.FEMALE
        ]

    @classmethod
    def roll_random(cls, amount=1):
        """Method docstring."""

        if not amount:
            return None

        results = [CharacterGender(s) for s in random.choices(cls.as_list(), k=amount)]
        return results[0] if amount == 1 else results


class CharacterGender(object):
    """Class docstring."""

    def __init__(self, gender):
        self.gender = gender

    def __str__(self):
        return f'Gender: {self.gender}'
