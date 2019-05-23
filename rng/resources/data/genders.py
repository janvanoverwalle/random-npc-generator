"""
Module docstring.
"""


class Genders(object):
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
