"""
Module docstring.
"""


class Strings(object):
    """Class docstring."""

    CR = '\r'
    LF = '\n'
    TAB = '\t'
    RANDOM = 'random'

    @classmethod
    def equals_ignore_case(cls, a, b):
        """Method docstring."""
        return a.lower() == b.lower()
