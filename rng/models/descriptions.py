"""
Module docstring.
"""
import json
import random
from pathlib import Path
from rng.helpers.definition_lookup import DefinitionLookup
from rng.resources.data.strings import Strings
from rng.helpers.utils import Utils


class CharacterDescriptions(object):
    """Class docstring."""

    TAG_OBJ_PN = '{object_pronoun}'
    TAG_SUB_PN = '{subject_pronoun}'
    TAG_POS_PN = '{prosessive_pronoun}'
    TAG_NOUN = '{noun}'
    TAG_ART = '{article}'
    TAG_ADJ = '{adjective}'
    TAG_ADV = '{adverb}'
    TAG_VERB = '{verb}'
    TAG_CONJ = '{conjunction}'

    repeat = lambda tag, mi, ma: f'{tag}:{{' + (str(mi) if mi else '0') + ':' + (str(ma) if ma else '9') + '}'

    KEY_ADJECTIVES = 'ADJECTIVE'
    KEY_ADVERBS = 'ADVERB'
    KEY_NOUNS = 'NOUN'
    KEY_VERBS = 'VERB'

    _json_path = Path(__file__).parent.parent / 'resources' / 'json' / 'character_descriptions.json'
    _description_data = {}

    _structure_map = [
        (
            TAG_POS_PN,
            repeat(TAG_ADJ, 0, 2),
            TAG_NOUN
        ),
        (
            TAG_POS_PN,
            repeat(TAG_ADJ, 0, 2),
            TAG_NOUN,
            TAG_CONJ,
            repeat(TAG_ADJ, 0, 2),
            TAG_NOUN
        )
    ]
    """
    cfg1.add_prod()
    cfg1.add_prod('NP', 'I | he | she | Joe')
    cfg1.add_prod()
    cfg1.add_prod('Det', 'a | the | my | his')
    cfg1.add_prod('N', 'elephant | cat | jeans | suit')
    cfg1.add_prod('V', 'kicked | followed | shot')
    """

    @classmethod
    def _load_json_data(cls, force_update=False):
        if cls._description_data and not force_update:
            return

        cls._description_data.clear()

        with open(f'{cls._json_path}', encoding='utf8') as json_file:
            cls._description_data = json.load(json_file)

    @classmethod
    def _generate_sentence_structure(cls):
        pass

    @classmethod
    def roll_random(cls, amount=1, gender=None, race=None):
        """Method docstring."""

        if not amount:
            return None

        cls._load_json_data()

        results = []
        for _ in range(amount):
            traits = {}
            for k, v in cls._description_data.items():
                if not v or random.randint(1, 10) < 9:
                    continue
                traits[k] = random.choice(v)
            results.append(CharacterDescription(traits))

        return results[0] if amount == 1 else results

    @classmethod
    def test(cls, gender=None, race=None):
        """Method docstring."""
        cls._load_json_data()

        sentence = []
        structure = random.choice(cls._structure_map)

        article = False
        for tag in structure:
            repeat = (1, 1)
            if ':' in tag:
                idx = tag.find(':')
                repeat = tuple([int(e) for e in tag[idx+2:-1].split(':')])

            rand_range = random.randint(repeat[0], repeat[1])
            print(rand_range)
            for _ in range(rand_range):
                if cls.TAG_OBJ_PN in tag:
                    sentence.append('it' if not gender else gender.object_pronoun)
                elif cls.TAG_SUB_PN in tag:
                    sentence.append('it' if not gender else gender.subject_pronoun)
                elif cls.TAG_POS_PN in tag:
                    sentence.append('its' if not gender else gender.possessive_pronoun)
                elif cls.TAG_NOUN in tag:
                    sentence.append(random.choice(cls._description_data[cls.KEY_NOUNS])['WORD'])
                elif cls.TAG_ART in tag:
                    article = True
                    sentence.append(cls.TAG_ART)
                elif cls.TAG_ADJ in tag:
                    sentence.append(random.choice(cls._description_data[cls.KEY_ADJECTIVES])['WORD'])
                elif cls.TAG_ADV in tag:
                    sentence.append(random.choice(cls._description_data[cls.KEY_ADVERBS])['WORD'])
                elif cls.TAG_VERB in tag:
                    sentence.append(random.choice(cls._description_data[cls.KEY_VERBS])['WORD'])
                elif cls.TAG_CONJ in tag:
                    sentence.append('and')

            if article:
                sentence[-2] = Utils.article_for(sentence[-1])
                article = False

        return ' '.join(sentence)


class CharacterDescription(object):
    """Class docstring."""

    def __init__(self, traits, definitions=None):
        self._generate_structure()
        self.traits = traits
        self._definitions = definitions

    def __str__(self):
        return f'{self.traits}'

    def __repr__(self):
        return str(self)

    def _generate_structure(self):
        pass

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

    def description(self):
        """Method docstring."""
        return ''
