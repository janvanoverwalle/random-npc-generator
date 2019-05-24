"""
Module docstring.
"""
import json
import random
from pathlib import Path
from rng.helpers.definition_lookup import DefinitionLookup


class CharacterDescriptions(object):
    """Class docstring."""

    EYES = 'EYES'
    EYES_COLOR = 'EYES_COLOR'
    EYEBROWS = 'EYEBROWS'
    SKIN = 'SKIN'
    SKIN_COLOR = 'SKIN_COLOR'
    FACE = 'FACE'
    NOSE = 'NOSE'
    MOUTH = 'MOUTH'
    FACIAL_HAIR = 'FACIAL_HAIR'
    HAIR = 'HAIR'
    HAIR_COLOR = 'HAIR_COLOR'
    BODY_TYPE = 'BODY_TYPE'
    HANDS = 'HANDS'

    _json_path = Path(__file__).parent.parent / 'resources' / 'json' / 'character_descriptions.json'
    _description_data = {}

    @classmethod
    def _load_json_data(cls, force_update=False):
        if cls._description_data and not force_update:
            return

        cls._description_data.clear()

        with open(f'{cls._json_path}', encoding='utf8') as json_file:
            cls._description_data = json.load(json_file)

    @classmethod
    def roll_random(cls, amount=1):
        """Method docstring."""

        if not amount:
            return None

        cls._load_json_data()

        # TODO: Finish

        results = []
        for _ in range(amount):
            traits = {}
            for k, v in cls._description_data.items():
                traits[k] = random.choice(v)
            results.append(CharacterDescription(traits))

        return results[0] if amount == 1 else results


class CharacterDescription(object):
    """Class docstring."""

    def __init__(self, traits, definition=None):
        self.traits = traits
        self._definition = definition

    def __str__(self):
        return f'{self.traits}'

    def __repr__(self):
        return str(self)

    @property
    def definition(self):
        """Method docstring."""
        if not self._definition:
            self._definition = DefinitionLookup.look_up(self.description)
        return self._definition
