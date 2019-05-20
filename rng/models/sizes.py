"""
Module docstring.
"""

class CreatureSize(object):
    """Class docstring."""

    NONE = 'none'
    TINY = 'tiny'
    SMALL = 'small'
    MEDIUM = 'medium'
    LARGE = 'large'
    HUGE = 'huge'
    GARGANTUAN = 'gargantuan'

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
