"""
Module docstring.
"""
import json
import random
import numpy
from pathlib import Path
from rng.helpers.definition_lookup import DefinitionLookup
from rng.resources.data.strings import Strings
from rng.helpers.utils import Utils


class CharacterDescriptions(object):
    """Class docstring."""

    _json_path = Path(__file__).parent.parent / 'resources' / 'json' / 'old_character_descriptions.json'
    _description_data = {}

    @classmethod
    def _load_json_data(cls, force_update=False):
        if cls._description_data and not force_update:
            return

        cls._description_data.clear()

        with open(f'{cls._json_path}', encoding='utf8') as json_file:
            cls._description_data = json.load(json_file)

    @classmethod
    def _calculate_distribution(cls, length=10):
        norm = numpy.random.normal(length/4, length/4, 10000)
        norm.sort()
        norm = [int(n+0.5)+1 for n in norm if 0 <= n+0.5 < length]
        freq = {}
        for n in norm:
            if n not in freq:
                freq[n] = 0
            freq[n] += 1
        return [v/len(norm)*100 for k, v in freq.items()]

    @classmethod
    def roll_random(cls, amount=1):
        """Method docstring."""

        if not amount:
            return None

        cls._load_json_data()

        results = []
        for _ in range(amount):            
            descr_key_count = len(cls._description_data.keys())
            population = range(0, descr_key_count)
            weights = cls._calculate_distribution(descr_key_count)
            amount_of_traits = random.choices(population, weights, k=1)[0]
            all_descr_keys = [k for k, v in cls._description_data.items()]
            trait_keys = random.choices(all_descr_keys, k=amount_of_traits)
            traits = {}
            for key in trait_keys:
                value = cls._description_data[key]
                if not value:
                    continue
                traits[key] = random.choice(value)
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

    def _unpack_kwargs(self, **kwargs):
        s = kwargs.get('subject')
        o = kwargs.get('object')
        p = kwargs.get('possessive')
        sp = kwargs.get('spacer')
        return s, o, p, sp

    def _readable_eyes(self, traits, **kwargs):
        sub_noun_str, obj_noun_str, pos_noun_str, spacer = self._unpack_kwargs(**kwargs)
        return 'TODO'

    def _readable_skin(self, traits, **kwargs):
        sub_noun_str, obj_noun_str, pos_noun_str, spacer = self._unpack_kwargs(**kwargs)
        return 'TODO'

    def _readable_face(self, traits, **kwargs):
        sub_noun_str, obj_noun_str, pos_noun_str, spacer = self._unpack_kwargs(**kwargs)
        return 'TODO'

    def _readable_hair(self, traits, **kwargs):
        sub_noun_str, obj_noun_str, pos_noun_str, spacer = self._unpack_kwargs(**kwargs)
        return 'TODO'

    def _readable_body(self, traits, **kwargs):
        sub_noun_str, obj_noun_str, pos_noun_str, spacer = self._unpack_kwargs(**kwargs)
        return 'TODO'

    def definition(self, trait):
        """Method docstring."""
        if trait not in self.traits.values():
            return None
        key = [k for k, v in self.traits.items() if v == trait]
        if not self._definitions:
            self._definitions = {}
        if not self._definitions.get(key):
            self._definitions[key] = DefinitionLookup.look_up_definition(trait)
        return self._definitions

    def readable_description(self, **kwargs):
        """Method docstring."""
        iterator = self.traits.items()
        description = [
            self._readable_eyes({k:v for k, v in iterator if 'EYE' in k}, **kwargs),
            self._readable_skin({k:v for k, v in iterator if 'SKIN' in k}, **kwargs),
            self._readable_face({k:v for k, v in iterator if k in ('FACE', 'NOSE', 'MOUTH')}, **kwargs),
            self._readable_hair({k:v for k, v in iterator if 'HAIR' in k}, **kwargs),
            self._readable_body({k:v for k, v in iterator if 'BODY' in k}, **kwargs)
        ]
        return ' '.join(description)
