"""
Module docstring.
"""


class Strings(object):
    """Class docstring."""

    CR = '\r'
    LF = '\n'
    TAB = '\t'
    RANDOM = 'random'
    EMPTY = ''

    @classmethod
    def equals_ignore_case(cls, s1, s2):
        """Method docstring."""
        return s1.lower() == s2.lower()

    @classmethod
    def is_vowel(cls, string):
        """Method docstring."""
        if not isinstance(string, str):
            string = str(string)
        return all([c.lower() in 'aeiou' for c in string])
