"""
Module docstring.
"""
import json
import random
from pathlib import Path
from rng.helpers.definition_lookup import DefinitionLookup


class CharacterQuirks(object):
    """Class docstring."""

    QUIRK = 'QUIRK'
    DEFINITION = 'DEFINITION'
    SENTENCES = 'SENTENCES'
    ADJECTIVES = 'ADJECTIVES'
    APPEARANCE = 'APPEARANCE'
    COLOR = 'COLOR'
    CONDITION = 'CONDITION'
    POSITIVE_PERSONALITY = 'POSITIVE_PERSONALITY'
    NEGATIVE_PERSONALITY = 'NEGATIVE_PERSONALITY'
    SHAPE = 'SHAPE'
    SIZE = 'SIZE'
    SOUND = 'SOUND'
    TIME = 'TIME'
    TASTE = 'TASTE'
    TOUCH = 'TOUCH'
    QUANTITY = 'QUANTITY'
    PERSONAL = 'PERSONAL'

    _json_path = Path(__file__).parent.parent / 'resources' / 'json' / 'character_quirks.json'
    _quirk_data = {}

    @classmethod
    def _load_json_data(cls, force_update=False):
        if cls._quirk_data and not force_update:
            return

        cls._quirk_data.clear()

        with open(f'{cls._json_path}', encoding='utf8') as json_file:
            cls._quirk_data = json.load(json_file)

    @classmethod
    def roll_random(cls, amount=1):
        """Method docstring."""

        if not amount:
            return None

        cls._load_json_data()

        adj_data = cls._quirk_data.get(cls.ADJECTIVES)
        if not adj_data:
            return None

        quirk_list = []
        for k, v in adj_data.items():
            if cls.PERSONAL not in k:
                continue
            quirk_list += v

        selected_quirks = [q for q in random.choices(quirk_list, k=amount)]
        results = []
        for q in selected_quirks:
            if not isinstance(q, dict):
                results.append(CharacterQuirk(q))
            else:
                results.append(CharacterQuirk(q.get(cls.QUIRK), q.get(cls.DEFINITION)))

        return results[0] if amount == 1 else results


class CharacterQuirk(object):
    """Class docstring."""

    def __init__(self, quirk, definition=None):
        self.quirk = quirk
        self._definition = definition

    def __str__(self):
        return f'{self.quirk}'

    def __repr__(self):
        return str(self)

    @property
    def definition(self):
        """Method docstring."""
        if not self._definition:
            self._definition = DefinitionLookup.look_up_definition(self.quirk)
        return self._definition
