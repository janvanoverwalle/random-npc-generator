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
        if not string:
            return Strings.EMPTY
        if not isinstance(string, str):
            string = str(string)
        string = string.strip().lower()
        if string.startswith(('a ', 'an ')):
            return Strings.EMPTY
        if Strings.is_vowel(string[0]):
            return 'an'
        return 'a'

    @classmethod
    def random_intensifier(cls, uniform=False):
        """Method docstring."""
        intensifiers = ['', 'rather', 'slightly', 'very', 'mostly', 'a bit']
        weights = ([1] * len(intensifiers)) if uniform else [5, 1, 1, 1, 1, 1]
        return random.choices(intensifiers, weights, k=1)[0]

    @classmethod
    def scan_for_values_with_key(cls, obj, key):
        """Method docstring."""
        if not obj:
            return None

        results = []
        if isinstance(obj, (list, tuple)):
            for elem in obj:
                result = cls.scan_for_values_with_key(elem, key)
                if result:
                    results += result
        elif isinstance(obj, dict):
            for k, v in obj.items():
                if k == key:
                    results.append(v)
                else:
                    result = cls.scan_for_values_with_key(v, key)
                    if result:
                        results += result
        return results
