"""
Module docstring.
"""


class Genders(object):
    """Class docstring."""

    KEY = 'gender'

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
    def is_valid(cls, obj):
        """Method docstring."""
        try:
            return obj.strip().lower() in cls.as_list()
        except Exception:
            return False

    @classmethod
    def to(cls, obj):
        try:
            for g in cls.as_list():
                if g.lower() == obj.lower():
                    return g
        except Exception:
            return obj
