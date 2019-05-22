"""
Module docstring.
"""
from rng.models.names import CharacterNames
from rng.models.professions import CharacterProfessions
from rng.models.races import CharacterRaces
from rng.models.genders import CharacterGenders
from rng.resources.objects.strings import Strings


class Character(object):
    """Class docstring."""

    NAME = 'name'
    GENDER = 'gender'
    RACE = 'race'
    PROFESSION = 'profession'
    JOB = 'job'

    def __init__(self, **kwargs):
        self.name = kwargs.get(self.NAME)
        self.gender = kwargs.get(self.GENDER)
        self.race = kwargs.get(self.RACE)
        self.profession = kwargs.get(self.PROFESSION, kwargs.get(self.JOB))

        self.race.roll_random_abilities()

    def __str__(self):
        string = (
            f'{self.name}{Strings.NEWLINE}'
            f'{self.gender}{Strings.NEWLINE}'
            f'{self.race}{Strings.NEWLINE}'
            f'{self.profession}'
        )
        return string

    @property
    def senses(self):
        """Method docstring."""
        return self.race.senses

    @property
    def languages(self):
        """Method docstring."""
        return self.race.languages

    @property
    def saving_throws(self):
        """Method docstring."""
        return self.profession.saving_throws

    @property
    def skills(self):
        """Method docstring."""
        return self.race.skills + self.profession.skills


class RandomCharacter(Character):
    """Class docstring."""

    def __init__(self):
        gender = CharacterGenders.roll_random()
        race = CharacterRaces.roll_random()
        profession = CharacterProfessions.roll_random('city')
        name = CharacterNames.roll_random(race, gender)
        kwargs = {
            self.NAME: name,
            self.GENDER: gender,
            self.RACE: race,
            self.PROFESSION: profession
        }
        super().__init__(**kwargs)
