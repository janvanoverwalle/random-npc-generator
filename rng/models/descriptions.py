"""
Module docstring.
"""
import json
import random
from pathlib import Path
import numpy
from rng.helpers.definition_lookup import DefinitionLookup
from rng.resources.data.strings import Strings
from rng.helpers.utils import Utils


class CharacterDescriptions(object):
    """Class docstring."""

    EYES = 'EYES'
    EYE_COLOR = 'EYE_COLOR'
    EYEBROWS = 'EYEBROWS'
    SKIN = 'SKIN'
    SKIN_COLOR = 'SKIN_COLOR'
    FACE = 'FACE'
    NOSE = 'NOSE'
    MOUTH = 'MOUTH'
    HAIR = 'HAIR'
    HAIR_COLOR = 'HAIR_COLOR'
    FACIAL_HAIR = 'FACIAL_HAIR'
    BODY_TYPE = 'BODY_TYPE'

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
            population = range(0, descr_key_count-1)
            weights = cls._calculate_distribution(descr_key_count-1)
            amount_of_traits = random.choices(population, weights, k=1)[0] + 1
            all_descr_keys = [k for k, v in cls._description_data.items()]
            trait_keys = random.sample(all_descr_keys, k=amount_of_traits)
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

    def _to_readable(self, acc, method, trait_dict, **kwargs):
        acc.append(method(trait_dict, **kwargs))
        if kwargs.get('full_details'):
            for k, v in trait_dict.items():
                if not v:
                    continue
                definition = self.definition(v)
                if not definition:
                    continue
                acc.append(f'  <{v.capitalize()}: {definition}>')

    def _unpack_kwargs(self, **kwargs):
        s = kwargs.get('subject')
        o = kwargs.get('object')
        p = kwargs.get('possessive')
        n = kwargs.get('noun')
        sp = kwargs.get('spacer')
        return s, o, p, n, sp

    def _combine_description_string(self, string, spacer=None):
        if not string:
            return Strings.EMPTY
        if not spacer:
            spacer = Strings.EMPTY
        return spacer + (' '.join([s for s in string if s])).replace(' \'', '\'')

    def _readable_eyes(self, traits, **kwargs):
        if not traits:
            return Strings.EMPTY
        sub_noun_str, _, _, _, spacer = self._unpack_kwargs(**kwargs)
        string = []
        # Traits
        eyes_trait = traits.get(CharacterDescriptions.EYES)
        eye_color_trait = traits.get(CharacterDescriptions.EYE_COLOR)
        eyebrows_trait = traits.get(CharacterDescriptions.EYEBROWS)
        amount_eyes = random.choices([0, 1, 2], [1, 49, 950], k=1)[0]
        amount_eyes_str = 'eye' + ('' if amount_eyes == 1 else 's')
        if eyes_trait or eye_color_trait or eyebrows_trait:
            if amount_eyes == 0:
                string += [
                    sub_noun_str,
                    'has',
                    'no',
                    amount_eyes_str
                ]
            else:
                string += [
                    sub_noun_str,
                    'has',
                    'a single' if amount_eyes == 1 else random.choice(['a pair of', ''])
                ]
        # Eyes
        if eyes_trait and amount_eyes > 0:
            string += [
                eyes_trait,
                amount_eyes_str
            ]
        # Eye Color
        if eye_color_trait and amount_eyes > 0:
            verbs = ['looks', 'appears', 'seems', 'is'] if amount_eyes == 1 else ['look', 'appear', 'seem', 'are']
            string += [
                amount_eyes_str if not eyes_trait else '',
                random.choice(['which', 'that']),
                random.choices(verbs, [2, 1, 1, 2], k=1)[0],
                eye_color_trait,
                'in',
                random.choice(['color', 'tone', 'hue'])
            ]
        # Eyebrows
        if eyebrows_trait:
            conjunction = ['and ' + ('is' if amount_eyes == 1 else 'are'), '']
            string += [
                amount_eyes_str if not eyes_trait and not eye_color_trait and amount_eyes > 0 else '',
                random.choice(conjunction) if (eyes_trait or eye_color_trait) and amount_eyes > 0 else '',
                random.choice(['framed by']),
                Utils.article_for(eyebrows_trait) if amount_eyes == 1 else '',
                eyebrows_trait,
                'eyebrow' + ('' if amount_eyes == 1 else 's')
            ]
        combined_string = self._combine_description_string(string, spacer)
        return combined_string

    def _readable_skin(self, traits, **kwargs):
        if not traits:
            return Strings.EMPTY
        _, _, pos_noun_str, _, spacer = self._unpack_kwargs(**kwargs)
        string = []
        # Traits
        skin_trait = traits.get(CharacterDescriptions.SKIN)
        skin_color_trait = traits.get(CharacterDescriptions.SKIN_COLOR)
        if skin_trait or skin_color_trait:
            string += [
                pos_noun_str,
                'skin',
                random.choices(['looks', 'appears', 'seems'], [2, 1, 1], k=1)[0],
            ]
        # Skin
        if skin_trait:
            string += [
                Utils.random_intensifier(),
                skin_trait
            ]
        # Skin Color
        if skin_color_trait:
            string += [
                'and' if skin_trait else '',
                Utils.random_intensifier(),
                skin_color_trait,
                'in',
                random.choice(['color', 'tone', 'tint', 'hue'])
            ]
        return self._combine_description_string(string, spacer)

    def _readable_face(self, traits, **kwargs):
        if not traits:
            return Strings.EMPTY
        sub_noun_str, _, pos_noun_str, _, spacer = self._unpack_kwargs(**kwargs)
        string = []
        # Traits
        face_trait = traits.get(CharacterDescriptions.FACE, Strings.EMPTY)
        nose_trait = traits.get(CharacterDescriptions.NOSE)
        mouth_trait = traits.get(CharacterDescriptions.MOUTH)
        face_portion = ' ' in face_trait
        # Face
        if face_trait:
            if face_portion and ' in ' in face_trait:
                idx = face_trait.find(' in ')+4
                face_trait = face_trait[:idx] + f'{pos_noun_str.lower()} ' + face_trait[idx:]
            plural = face_trait.endswith('s')
            string += [
                sub_noun_str if face_portion else pos_noun_str,
                'has' if face_portion else 'face',
                Utils.article_for(face_trait) if face_portion and not plural else '',
                '' if face_portion else random.choices(['looks', 'appears', 'seems'], [2, 1, 1], k=1)[0],
                '' if face_portion else Utils.random_intensifier(),
                face_trait
            ]
        # Nose
        if nose_trait:
            connector = 'adorned with' if not face_portion else 'along with'
            string += [
                connector if face_trait else sub_noun_str,
                '' if face_trait else 'has',
                Utils.article_for(nose_trait),
                nose_trait,
                'nose'
            ]
        # Mouth
        if mouth_trait:
            physical = ' ' in mouth_trait
            physical_pre = 'a mouth' if mouth_trait.startswith('with') and physical else ''
            if 'between' in mouth_trait:
                idx = mouth_trait.find('between')+8
                mouth_trait = mouth_trait[:idx] + f'{pos_noun_str.lower()} ' + mouth_trait[idx:]

            if face_trait and nose_trait:
                string.append('and')
            elif face_trait:
                string.append(f'and {sub_noun_str.lower()} has')
            elif nose_trait:
                string.append('along with')
            else:
                string.append(f'{sub_noun_str} has')

            string += [
                physical_pre if physical else Utils.article_for(mouth_trait),
                mouth_trait,
                '' if physical else 'mouth'
            ]
        return self._combine_description_string(string, spacer)

    def _readable_hair(self, traits, **kwargs):
        if not traits:
            return Strings.EMPTY
        sub_noun_str, _, pos_noun_str, _, spacer = self._unpack_kwargs(**kwargs)
        string = []
        # Traits
        hair_trait = traits.get(CharacterDescriptions.HAIR, Strings.EMPTY)
        hair_color_trait = traits.get(CharacterDescriptions.HAIR_COLOR)
        facial_hair_trait = traits.get(CharacterDescriptions.FACIAL_HAIR)
        inv_hair_trait = '-' in hair_trait
        noun_hair_trait = hair_trait.startswith('a ') or hair_trait.startswith('an ')
        # Hair
        if hair_trait:
            string += [
                pos_noun_str if inv_hair_trait else sub_noun_str,
                'hair is' if inv_hair_trait else 'has',
                Utils.article_for(hair_trait) if noun_hair_trait else '',
                '' if not noun_hair_trait else hair_trait.split(' ')[0],
                hair_trait if not noun_hair_trait else ' '.join(hair_trait.split(' ')[1:]),
                '' if inv_hair_trait or noun_hair_trait else 'hair'
            ]
        # Hair Color
        if hair_color_trait:
            if hair_trait:
                insert_index = -1

                if noun_hair_trait:
                    string[-3] = Utils.article_for(hair_color_trait)
                    insert_index = -2
                elif inv_hair_trait:
                    string.insert(-1, 'with')
                    string.insert(-1, Utils.article_for(hair_color_trait))
                else:
                    string[-2] += ','

                string.insert(insert_index, hair_color_trait)

                if inv_hair_trait:
                    string.insert(-1, random.choice(['color', 'tone', 'hue']))
            else:
                string += [
                    sub_noun_str,
                    'has',
                    hair_color_trait,
                    random.choice(['colored', 'hued', '']),
                    'hair'
                ]
        # Facial Hair
        if facial_hair_trait:
            any_prev_traits = hair_trait or hair_color_trait
            shaven = 'shaven' in facial_hair_trait
            use_adjectives = len(facial_hair_trait.split(' ')) == 2
            adjective = random.choice(['grand', 'small', 'large', 'short', 'full', ''])
            string += [
                ('and' if shaven else 'with') if any_prev_traits else sub_noun_str,
                ('is' if shaven else '') if any_prev_traits else 'has',
                Utils.article_for(adjective) if use_adjectives else '',
                adjective if use_adjectives else '',
                facial_hair_trait.split(' ')[1] if use_adjectives else facial_hair_trait
            ]
        return self._combine_description_string(string, spacer)

    def _readable_body(self, traits, **kwargs):
        if not traits:
            return Strings.EMPTY
        sub_noun_str, _, _, noun_str, spacer = self._unpack_kwargs(**kwargs)
        string = []
        # Traits
        body_type_trait = traits.get(CharacterDescriptions.BODY_TYPE)
        # Body Type        
        if body_type_trait:
            intensifier = Utils.random_intensifier()
            if intensifier and intensifier == 'a bit':
                intensifier += ' of ' + Utils.article_for(body_type_trait)
            noun = random.choice(['body', 'figure', noun_str])
            article = Utils.article_for(intensifier) if intensifier else Utils.article_for(body_type_trait)
            string += [
                sub_noun_str,
                random.choice(['\'s', 'is']) if noun == noun_str else 'has',
                Utils.article_for(noun) if ' ' in body_type_trait else '',
                noun if ' ' in body_type_trait else '',
                ('of' if Strings.is_vowel(body_type_trait[0]) else 'with') if ' ' in body_type_trait else '',
                article if ' ' not in body_type_trait else '',
                intensifier if ' ' not in body_type_trait else '',
                body_type_trait,
                noun if ' ' not in body_type_trait else '',
                random.choice(['of body', '']) if noun == noun_str else ''
            ]
        return self._combine_description_string(string, spacer)

    @property
    def definitions(self):
        """Method docstring."""
        return self._definitions

    def definition(self, trait):
        """Method docstring."""
        key = None
        if trait in self.traits.keys():
            key = trait
        elif trait not in self.traits.values():
            return None

        if not key:
            key = [k for k, v in self.traits.items() if v == trait][0]
        else:
            trait = self.traits.get(key)

        if not self._definitions:
            self._definitions = {}

        if not self._definitions.get(key):
            self._definitions[key] = DefinitionLookup.look_up_definition(trait)

        # Write these to the JSON
        return self._definitions[key]

    def readable_description(self, **kwargs):
        """Method docstring."""
        description = []
        iterator = self.traits.items()

        eye_traits = {k:v for k, v in iterator if 'EYE' in k}
        self._to_readable(description, self._readable_eyes, eye_traits, **kwargs)

        skin_traits = {k:v for k, v in iterator if 'SKIN' in k}
        self._to_readable(description, self._readable_skin, skin_traits, **kwargs)

        face_traits = {k:v for k, v in iterator if k in ('FACE', 'NOSE', 'MOUTH')}
        self._to_readable(description, self._readable_face, face_traits, **kwargs)

        hair_traits = {k:v for k, v in iterator if 'HAIR' in k}
        self._to_readable(description, self._readable_hair, hair_traits, **kwargs)

        body_traits = {k:v for k, v in iterator if 'BODY' in k}
        self._to_readable(description, self._readable_body, body_traits, **kwargs)

        return [d for d in description if d]

    def has_facial_hair(self):
        """Method docstring."""
        return CharacterDescriptions.FACIAL_HAIR in self.traits

    def remove_facial_hair(self):
        """Method docstring."""
        if not self.has_facial_hair():
            return
        del self.traits[CharacterDescriptions.FACIAL_HAIR]
