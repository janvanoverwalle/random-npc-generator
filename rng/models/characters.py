"""
Module docstring.
"""
import json
import random
from rng.helpers.utils import Utils
from rng.models.names import CharacterNames
from rng.models.classes import CharacterClasses
from rng.models.professions import CharacterProfessions
from rng.models.descriptions import CharacterDescriptions
from rng.models.races import CharacterRaces
from rng.models.genders import CharacterGenders
from rng.models.quirks import CharacterQuirks
from rng.resources.data.strings import Strings


class Characters(object):
    """Class docstring."""

    PC = 'PC'
    NPC = 'NPC'

    _type_to_character_map = None

    @classmethod
    def get(cls, class_name):
        """Method docstring."""
        if not cls._type_to_character_map:
            cls._type_to_character_map = {
                cls.PC: RandomPC,
                cls.NPC: RandomNPC
            }

        if not isinstance(class_name, (list, tuple)):
            class_name = [class_name]

        characters = []
        for name in class_name:
            if not name or Strings.equals_ignore_case(name, Strings.RANDOM):
                characters += [v for k, v in cls._type_to_character_map.items() if v not in characters]
            else:
                name = cls._type_to_character_map.get(name)
                if name not in characters:
                    characters.append(name)
        return characters

    @classmethod
    def roll(cls, character_type=None, amount=1, **kwargs):
        """Method docstring."""
        if not amount:
            return None

        available_characters = cls.get(character_type)

        results = [random.choice(c)(**kwargs) if isinstance(c, list) else c() for c in random.choices(available_characters, k=amount)]
        return results[0] if amount == 1 else results

    @classmethod
    def roll_pc(cls, amount=1, **kwargs):
        """Method docstring."""
        return cls.roll(cls.PC, amount, **kwargs)

    @classmethod
    def roll_npc(cls, amount=1, **kwargs):
        """Method docstring."""
        return cls.roll(cls.NPC, amount, **kwargs)

    @classmethod
    def roll_random(cls, amount=1, **kwargs):
        """Method docstring."""
        return cls.roll(Strings.RANDOM, amount, **kwargs)


class Character(object):
    """Class docstring."""

    NAME = 'name'
    GENDER = 'gender'
    RACE = 'race'
    CLASS = 'class'
    LOCALE = 'locale'
    PROFESSION = 'profession'
    JOB = 'job'
    QUIRKS = 'quirks'
    DESCRIPTION = 'description'

    def __init__(self, **kwargs):
        self._name = kwargs.get(self.NAME)
        self._gender = kwargs.get(self.GENDER)
        self._race = kwargs.get(self.RACE)
        self._class = kwargs.get(self.CLASS)
        self._profession = kwargs.get(self.PROFESSION, kwargs.get(self.JOB))
        quirks = kwargs.get(self.QUIRKS)
        self._quirks = quirks if isinstance(quirks, (list, tuple)) else [quirks]
        self._description = kwargs.get(self.DESCRIPTION)

        self._race.roll_random_abilities()
        self._race.roll_age(self._class)

    def __str__(self):
        string = f'{self._name}, '
        string += f'a {self._gender} {self._race.name} '
        string += Strings.LF
        return string

    def _age_description(self, full_details=True, standalone=True):
        if standalone:
            subject = self._name.first_name
        else:
            subject = f'  {self._gender.subject_pronoun.capitalize()}'
        s = 's' if full_details else ''
        age_article = ('an' if str(self.age.current).startswith('8') else 'a')
        string = (
            f'{subject} is {age_article}'
            f' {self.age.current} year{s} old'
        )
        if full_details:
            string += f' {self.age.age_description()}'
        return string

    def _class_description(self, full_details=True, standalone=True):
        if standalone:
            subject = self._name.first_name
        else:
            subject = ' ' + random.choice(['who', 'and', 'working'])
        verb = 'as ' if subject.endswith('ing') else random.choice(['works as', 'is']) + ' '
        string = f'{subject} {verb}'
        if self._class:
            job_name = f'{self._class.name}'
        if self._profession:
            job_name = f'{self._profession.name}'
        string += Utils.article_for(job_name)
        string += f' {job_name}'
        string += Strings.LF
        if full_details:
            if self._class:
                job_descr = f'{self._class.description}'
            if self._profession:
                job_descr = f'{self._profession.description}'
            string += f'    <{job_name}: {job_descr}>'
            string += Strings.LF
        return string

    def _character_descriptions(self, full_details, standalone=True):
        if standalone:
            subject_str = self._name.first_name
            object_str = self._name.first_name
            possessive_str = self._name.first_name + '\''
            if possessive_str[0].lower() not in 's':
                possessive_str += 's'
            spacer = ''
        else:
            subject_str = self._gender.subject_pronoun.capitalize()
            object_str = self._gender.object_pronoun.capitalize()
            possessive_str = self._gender.possessive_pronoun.capitalize()
            spacer = '  '
        noun_str = self._gender.noun
        kwargs = {
            'subject': subject_str,
            'object': object_str,
            'possessive': possessive_str,
            'noun': noun_str,
            'full_details': full_details
        }
        readable_descriptions = self._description.readable_description(**kwargs)
        readable_str = f'{Strings.LF}{spacer}'.join(readable_descriptions)
        return (spacer + readable_str + Strings.LF) if readable_descriptions else Strings.EMPTY

    def _quirk_descriptions(self, full_details, standalone=True):
        if standalone:
            subject = self._name.first_name
        else:
            subject = f'  {self._gender.subject_pronoun.capitalize()}'
        quirks = self._quirks if isinstance(list, tuple) else [self._quirks]
        string = ''
        for quirk in quirks:
            string += subject
            verb = random.choice([' tends to be', '\'s considered to be', '\'s known to be', '\'s'])
            intensifier = Utils.random_intensifier()
            if intensifier:
                if intensifier == 'a bit':
                    intensifier += ' of ' + Utils.article_for(quirk)
                intensifier += ' '
            article = Utils.article_for(intensifier) if intensifier else Utils.article_for(quirk)
            if article:
                article += ' '
            string += f'{verb} {article}{intensifier}{quirk} person'
            string += Strings.LF
            if full_details:
                string += f'    <{quirk.quirk.capitalize()}: {quirk.definition}>'
                string += Strings.LF
        return string

    @property
    def name(self):
        """Method docstring."""
        return self._name

    @property
    def gender(self):
        """Method docstring."""
        return self._gender

    @property
    def race(self):
        """Method docstring."""
        return self._race

    @property
    def cclass(self):
        """Method docstring."""
        return self._class

    @property
    def profession(self):
        """Method docstring."""
        return self._profession

    @property
    def class_or_profession(self):
        """Method docstring."""
        return self._class if self._class else self._profession

    @property
    def quirks(self):
        """Method docstring."""
        return self._quirks

    @property
    def age(self):
        """Method docstring."""
        return self._race.age

    @property
    def languages(self):
        """Method docstring."""
        ret = set()
        if self._class:
            ret = ret.union(set(self._class.languages))
        if self._race:
            ret = ret.union(set(self._race.languages))
        return list(ret)

    @property
    def saving_throws(self):
        """Method docstring."""
        ret = set()
        if self._class:
            ret = ret.union(set(self._class.saving_throws))
        if self._profession:
            ret = ret.union(set(self._profession.saving_throws))
        return list(ret)

    @property
    def senses(self):
        """Method docstring."""
        ret = set()
        if self._race:
            ret = ret.union(set(self._race.senses))
        return list(ret)

    @property
    def skills(self):
        """Method docstring."""
        ret = set()
        if self._profession:
            ret = ret.union(set(self._profession.skills))
        if self._race:
            ret = ret.union(set(self._race.skills))
        return list(ret)

    def to_json(self):
        """Method docstring."""
        data = {
            'name': self.name.name,
            'gender': self.gender.gender,
            'race': self.race.name,
            'class': self.cclass.name if self.cclass else None,
            'profession': self.profession.name if self.profession else None,
            'quirks': [q.quirk for q in self.quirks],
            'age': self.age.current,
            'languages': self.languages,
            'saving_throws': self.saving_throws,
            'senses': [s.name for s in self.senses],
            'skills': self.skills
        }
        return data

    def has_class(self):
        """Method docstring."""
        return self._class is not None

    def has_profession(self):
        """Method docstring."""
        return self._profession is not None

    def description(self):
        """Method docstring."""
        return str(self)

    def detailed_description(self, full_details=True):
        """Method docstring."""
        string = str(self)
        string += self._age_description(full_details, standalone=False)
        string += self._class_description(full_details, standalone=False)
        string += self._character_descriptions(full_details, standalone=False)
        string += self._quirk_descriptions(full_details, standalone=False)
        return string

    def shave(self):
        """Method docstring."""
        self._description.remove_facial_hair()


class RandomNPC(Character):
    """Class docstring."""

    def __init__(self, **kwargs):
        gender = kwargs.get(self.GENDER, CharacterGenders.roll_random())
        race = kwargs.get(self.RACE, CharacterRaces.roll_random())
        locales = kwargs.get(self.LOCALE)
        if not locales:
            locales = ['City', 'Village', 'Outskirts']
        rand_locale = random.choice(locales)
        profession = kwargs.get(self.PROFESSION, CharacterProfessions.roll_random(rand_locale))
        name = kwargs.get(self.NAME, CharacterNames.roll_random(race, gender))
        quirks = kwargs.get(self.QUIRKS, CharacterQuirks.roll_random())
        description = kwargs.get(self.DESCRIPTION, CharacterDescriptions.roll_random())
        kwargs = {
            self.NAME: name,
            self.GENDER: gender,
            self.RACE: race,
            self.PROFESSION: profession,
            self.QUIRKS: quirks,
            self.DESCRIPTION: description
        }
        super().__init__(**kwargs)

        if self._gender.is_female():
            self.shave()


class RandomPC(Character):
    """Class docstring."""

    def __init__(self, **kwargs):
        gender = kwargs.get(self.GENDER, CharacterGenders.roll_random())
        race = kwargs.get(self.RACE, CharacterRaces.roll_random())
        char_class = kwargs.get(self.CLASS, CharacterClasses.roll_random())
        name = kwargs.get(self.NAME, CharacterNames.roll_random(race, gender))
        quirks = kwargs.get(self.QUIRKS, CharacterQuirks.roll_random())
        description = kwargs.get(self.DESCRIPTION, CharacterDescriptions.roll_random())
        kwargs = {
            self.NAME: name,
            self.GENDER: gender,
            self.RACE: race,
            self.CLASS: char_class,
            self.QUIRKS: quirks,
            self.DESCRIPTION: description
        }
        super().__init__(**kwargs)
