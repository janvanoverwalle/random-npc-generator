"""
Module docstring.
"""
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
        self._quirks = kwargs.get(self.QUIRKS)
        self._description = kwargs.get(self.DESCRIPTION)

        self._race.roll_random_abilities()
        self._race.roll_age(self._class)

    def __str__(self):
        string = f'{self._name}, '
        string += f'a {self._gender} {self._race.name} '
        string += Strings.LF
        return string

    def description(self):
        """Method docstring."""
        return str(self)

    def long_description(self, detail_descriptions=True):
        """Method docstring."""
        string = str(self)
        string += self._age_description(detail_descriptions, independent=False)
        string += self._class_description(detail_descriptions, independent=False)
        string += self._character_descriptions(detail_descriptions, independent=False)
        string += self._quirk_descriptions(detail_descriptions, independent=False)
        return string

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
            ret = ret.union(set(self._profession.saving_throws))
        if self._race:
            ret = ret.union(set(self._race.saving_throws))
        return list(ret)

    def _age_description(self, detail_descriptions=True, independent=True):
        if independent:
            subject = self._name.first_name
        else:
            subject = f'  {self._gender.subject_pronoun.capitalize()}'
        s = 's' if detail_descriptions else ''
        string = (
            f'{subject} is a'
            f' {self.age.current} year{s} old'
        )
        if detail_descriptions:
            string += f' {self.age.age_description()}'
        return string

    def _class_description(self, detail_descriptions=True, independent=True):
        if independent:
            subject = self._name.first_name
        else:
            subject = ' who'
        string = f'{subject} works as '
        if self._class:
            job_name = f'{self._class.name}'
        if self._profession:
            job_name = f'{self._profession.name}'
        string += Utils.article_for(job_name)
        string += f' {job_name}'
        string += Strings.LF
        if detail_descriptions:
            if self._class:
                job_descr = f'{self._class.description}'
            if self._profession:
                job_descr = f'{self._profession.description}'
            string += f'    <{job_name}: {job_descr}>'
            string += Strings.LF
        return string

    def _character_descriptions(self, detail_descriptions, independent=True):
        # TODO: Finish
        return ''

    def _quirk_descriptions(self, detail_descriptions, independent=True):
        if independent:
            subject = self._name.first_name
        else:
            subject = f'  {self._gender.subject_pronoun.capitalize()}'
        quirks = self._quirks if isinstance(list, tuple) else [self._quirks]
        string = ''
        for quirk in quirks:
            string += f'{subject}'
            adverb = random.choices(['', 'very ', 'a bit of a ', 'rather '], [7, 1, 1, 1], k=1)[0]
            article = Utils.article_for(adverb) if adverb else Utils.article_for(quirk)
            string += f' tends to be {article} {adverb}{quirk} person'
            string += Strings.LF
            if detail_descriptions:
                string += f'    <{quirk.quirk.capitalize()}: {quirk.definition}>'
                string += Strings.LF
        return string


class RandomNPC(Character):
    """Class docstring."""

    def __init__(self, **kwargs):
        gender = kwargs.get(self.GENDER, CharacterGenders.roll_random())
        race = kwargs.get(self.RACE, CharacterRaces.roll_random())
        locales = ['City', 'Village', 'Outskirts']
        profession = kwargs.get(self.PROFESSION, CharacterProfessions.roll_random(random.choice(locales)))
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


class RandomPC(Character):
    """Class docstring."""

    def __init__(self):
        gender = CharacterGenders.roll_random()
        race = CharacterRaces.roll_random()
        char_class = CharacterClasses.roll_random()
        name = CharacterNames.roll_random(race, gender)
        quirks = CharacterQuirks.roll_random()
        description = CharacterDescriptions.roll_random()
        kwargs = {
            self.NAME: name,
            self.GENDER: gender,
            self.RACE: race,
            self.CLASS: char_class,
            self.QUIRKS: quirks,
            self.DESCRIPTION: description
        }
        super().__init__(**kwargs)
