"""
Module docstring.
"""


class Strings(object):
    """Class docstring."""

    NEWLINE = '\n'
    TAB = '\t'
    RANDOM = 'random'

    @classmethod
    def equals_ignore_case(cls, a, b):
        """Method docstring."""
        return a.lower() == b.lower()
