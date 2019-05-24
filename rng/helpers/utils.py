"""
Module docstring.
"""


class Utils(object):
    """Class docstring."""

    @classmethod
    def char_is_vowel(cls, char):
        """Method docstring."""
        return char.lower() in 'aeiou'

    @classmethod
    def string_is_vowel(cls, string):
        """Method docstring."""
        if not isinstance(string, str):
            string = str(string)
        return all([cls.char_is_vowel(c) for c in string])

    @classmethod
    def article_for(cls, string):
        """Method docstring."""
        if not isinstance(string, str):
            string = str(string)
        if string.lower().startswith(('a ', 'an ')):
            return ''
        if cls.char_is_vowel(string[0]):
            return 'an'
        return 'a'
