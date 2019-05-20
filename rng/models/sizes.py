"""
Module docstring.
"""

class Size(object):
    """Class docstring."""

    NONE = 'none'
    TINY = 'Tiny'
    SMALL = 'Small'
    MEDIUM = 'Medium'
    LARGE = 'Large'
    HUGE = 'Huge'
    GARGANTUAN = 'Gargantuan'

    @classmethod
    def as_list(cls):
        """Method docstring."""
        return [
            cls.TINY,
            cls.SMALL,
            cls.MEDIUM,
            cls.LARGE,
            cls.HUGE,
            cls.GARGANTUAN
        ]

    @classmethod
    def iterate(cls):
        """Method docstring."""
        for size in cls.as_list():
            yield size
