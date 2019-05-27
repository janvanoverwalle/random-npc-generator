"""
Module docstring.
"""
import json
import requests


class DefinitionLookup(object):
    """Class docstring."""

    MEANING = 'meaning'

    ADJECTIVE = 'adjective'
    ADVERB = 'adverb'
    CONJUNCTION = 'conjunction'
    INTERJECTION = 'interjection'
    NOUN = 'noun'
    PREPOSITION = 'preposition'
    PRONOUN = 'pronoun'
    VERB = 'verb'
    EXCLAMATION = 'exclamation'

    DEFINITION = 'definition'
    EXAMPLE = 'example'
    SYNONYMS = 'synonyms'

    @classmethod
    def meaning_of(cls, word):
        """Method docstring."""
        if not isinstance(word, str):
            word = str(word)
        word = word.lower().replace(' ', '+')

        url = f'https://googledictionaryapi.eu-gb.mybluemix.net/?define={word}&lang=en'
        response = requests.get(url)
        try:
            json_obj = json.loads(response.content)[0]
        except json.decoder.JSONDecodeError:
            return None
        return json_obj.get(cls.MEANING)

    @classmethod
    def look_up_definition(cls, word, part=None):
        """Method docstring."""
        meaning = cls.meaning_of(word)
        if not part:
            all_parts = meaning.keys()
            part = all_parts[0]
        part_data = meaning.get(part)
        results = [p.get(cls.DEFINITION) for p in part_data]
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
