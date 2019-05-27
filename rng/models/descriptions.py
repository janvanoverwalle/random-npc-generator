"""
Module docstring.
"""
import json
import random
from pathlib import Path
from rng.helpers.definition_lookup import DefinitionLookup
from rng.resources.data.strings import Strings


class CharacterDescriptions(object):
    """Class docstring."""

    ADJECTIVES = 'ADJECTIVES'
    ADVERBS = 'ADVERBS'
    NOUNS = 'NOUNS'
    VERBS = 'VERBS'

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
    def roll_random(cls, amount=1, gender=None):
        """Method docstring."""

        if not amount:
            return None

        cls._load_json_data()

        results = []
        for _ in range(amount):
            traits = {}
            for k, v in cls._description_data.items():
                if gender and gender.is_female() and k == CharacterDescriptions.FACIAL_HAIR:
                    continue
                if random.randint(1, 10) < 9:
                    continue
                traits[k] = random.choice(v)
            results.append(CharacterDescription(traits))

        return results[0] if amount == 1 else results


class CharacterDescription(object):
    """Class docstring."""

    def __init__(self, traits, definitions=None):
        self.traits = traits
        self._definitions = definitions

    def __str__(self):
        return f'{self.traits}'

    def __repr__(self):
        return str(self)

    def definition(self, trait):
        """Method docstring."""
        if trait not in self.traits.values():
            return None
        key = [k for k, v in self.traits.items() if v == trait]
        if not self._definitions:
            self._definitions = {}
        if not self._definitions.get(key):
            self._definitions[key] = DefinitionLookup.look_up(trait)
        return self._definitions

    def description(self):
        """Method docstring."""
        description_strings = []
        # Eyes
        descr = ''
        eye_traits = [
            self.traits.get(CharacterDescriptions.EYES),
            self.traits.get(CharacterDescriptions.EYES_COLOR)
        ]
        eye_descr = ', '.join([d for d in eye_traits if d])
        if eye_descr:
            descr += f'{{Subject}} has {eye_descr} eyes'
        # Eyebrows
        eyebrow_traits = self.traits.get(CharacterDescriptions.EYEBROWS)
        if eyebrow_traits:
            if not eye_descr:
                descr += f'{{Possessive}} eyes are'
            descr += f' framed by {eyebrow_traits} eyebrows'
        if descr and (eye_descr or eyebrow_traits):
            descr += f'.'
        if descr:
            description_strings.append(descr)

        # Skin
        descr = ''
        skin_traits = self.traits.get(CharacterDescriptions.SKIN)
        verb = random.choice(['is', 'looks', 'seems', 'appears'])
        if skin_traits:
            descr += f'{{Possessive}} skin {verb} {skin_traits}'
        skin_color = self.traits.get(CharacterDescriptions.SKIN_COLOR)
        if skin_color:
            if not skin_traits:
                descr += f'{{Possessive}} skin {verb} '
            else:
                descr += ' and '
            descr += f'{skin_color} in color'
        else:
            if skin_traits:
                descr = ''
                if not description_strings:
                    description_strings.append('')
                prev_descr = description_strings[-1]
                has = 'has ' if eyebrow_traits else ''
                prev_descr = f'{prev_descr[:-1]} and {has}{skin_traits} skin.'
                description_strings[-1] = prev_descr
        if descr and (skin_traits or skin_color):
            descr += f'.'
        if descr:
            description_strings.append(descr)

        # Face
        descr = ''
        face_traits = self.traits.get(CharacterDescriptions.FACE)
        if face_traits:
            if ' ' in face_traits:
                pass
            else:
                pass

        return (f'{Strings.LF}'.join(description_strings)) + Strings.LF
