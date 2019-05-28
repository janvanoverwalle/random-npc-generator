"""
Module docstring.
"""
import random
from rng.resources.data.strings import Strings


class Utils(object):
    """Class docstring."""

    @classmethod
    def article_for(cls, string):
        """Method docstring."""
        if not isinstance(string, str):
            string = str(string)
        if string.lower().startswith(('a ', 'an ')):
            return ''
        if Strings.is_vowel(string[0]):
            return 'an'
        return 'a'

    @classmethod
    def random_intensifier(cls, uniform=False):
        """Method docstring."""
        intensifiers = ['', 'rather', 'slightly', 'very', 'mostly', 'a bit']
        weights = ([1] * len(intensifiers)) if uniform else [5, 1, 1, 1, 1, 1]
        return random.choices(intensifiers, weights, k=1)[0]
