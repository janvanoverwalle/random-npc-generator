"""
Module docstring.
"""
import random
from rng.models.names import CharacterNames
from rng.models.professions import CharacterProfessions
from rng.models.races import CharacterRaces
from rng.models.genders import CharacterGenders
from rng.resources.data.strings import Strings


class Character(object):
    """Class docstring."""

    NAME = 'name'
    GENDER = 'gender'
    RACE = 'race'
    CLASS = 'class'
    PROFESSION = 'profession'
    JOB = 'job'

    def __init__(self, **kwargs):
        self._name = kwargs.get(self.NAME)
        self._gender = kwargs.get(self.GENDER)
        self._race = kwargs.get(self.RACE)
        self._class = kwargs.get(self.CLASS)
        self._profession = kwargs.get(self.PROFESSION, kwargs.get(self.JOB))

        self._race.roll_random_abilities()
        self._race.roll_age(self._class)

    def __str__(self):
        string = f'{self._name}, '
        string += f'a {self._gender} {self._race.name} '
        string += 'who is a'
        if self._class:
            job_name = f'{self._class.name}'
        if self._profession:
            job_name = f'{self._profession.name}'
        if job_name.lower()[0] in 'aeiou':
            string += 'n'
        string += f' {job_name}'
        string += f'{Strings.LF}'
        return string

    def description(self):
        """Method docstring."""
        return str(self)

    def long_description(self):
        """Method docstring."""
        string = str(self)
        string += f'  {self._name.first_name} is {self.age.current} years old'
        string += f' which makes {self._gender.pronoun} {self.age.age_description()}'
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


class RandomNPC(Character):
    """Class docstring."""

    def __init__(self):
        gender = CharacterGenders.roll_random()
        race = CharacterRaces.roll_random()
        locales = ['City', 'Village', 'Outskirts']
        profession = CharacterProfessions.roll_random(random.choice(locales))
        name = CharacterNames.roll_random(race, gender)
        kwargs = {
            self.NAME: name,
            self.GENDER: gender,
            self.RACE: race,
            self.PROFESSION: profession
        }
        super().__init__(**kwargs)


class RandomPC(Character):
    """Class docstring."""

    def __init__(self):
        gender = CharacterGenders.roll_random()
        race = CharacterRaces.roll_random()
        char_class = None
        name = CharacterNames.roll_random(race, gender)
        kwargs = {
            self.NAME: name,
            self.GENDER: gender,
            self.RACE: race,
            self.CLASS: char_class
        }
        super().__init__(**kwargs)
