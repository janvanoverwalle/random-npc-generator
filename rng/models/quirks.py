"""
Module docstring.
"""
import json
from pathlib import Path


class CharacterQuirks(object):
    """Class docstring."""

    _json_path = Path(__file__).parent.parent / 'resources' / 'json' / 'character_quirks.json'
    _quirk_data = {}

    @classmethod
    def _load_json_data(cls, force_update=False):
        if cls._name_data and not force_update:
            return

        cls._name_data.clear()

        with open(f'{cls._json_path}', encoding='utf8') as json_file:
            cls._name_data = json.load(json_file)

    @classmethod
    def roll_random(cls, amount=1):
        """Method docstring."""

        if not amount:
            return None

        pass


class CharacterQuirk(object):
    """Class docstring."""

    def __init__(self, quirk):
        self.quirk = quirk

    def __str__(self):
        return f'{self.quirk}'

    def __repr__(self):
        return str(self)
