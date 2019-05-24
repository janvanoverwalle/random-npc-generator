"""
Module docstring.
"""
import json
import requests


class DefinitionLookup(object):
    """Class docstring."""

    @classmethod
    def look_up(cls, word):
        """Method docstring."""
        if not isinstance(word, str):
            word = str(word)

        url = f'https://googledictionaryapi.eu-gb.mybluemix.net/?define={word.lower()}&lang=en'
        response = requests.get(url)
        json_obj = json.loads(response.content)
        results = cls._scan_for_key(json_obj, 'definition')
        return results[0] if results else None

    @classmethod
    def _scan_for_key(cls, obj, key):
        """Method docstring."""
        if not obj:
            return None

        results = []
        if isinstance(obj, (list, tuple)):
            for elem in obj:
                result = cls._scan_for_key(elem, key)
                if result:
                    results += result
        elif isinstance(obj, dict):
            for k, v in obj.items():
                if k == key:
                    results.append(v)
                else:
                    result = cls._scan_for_key(v, key)
                    if result:
                        results += result
        return results
