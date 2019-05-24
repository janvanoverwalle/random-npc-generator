"""
Module docstring.
"""
from rng.models.characters import RandomNPC
from rng.models.names import CharacterNames
from rng.models.professions import CharacterProfessions
from rng.models.races import CharacterRaces
from rng.models.genders import CharacterGenders
from rng.resources.data.races import Races


def roll_independently():
    """Function docstring."""

    # Gender
    rolled_gender = CharacterGenders.roll_random()

    # Race
    rolled_race = CharacterRaces.roll_random()
    # rolled_race = CharacterRaces.roll(CharacterRaces.DRAGONBORN)

    # Profession
    rolled_profession = CharacterProfessions.roll_random('city')

    # Name
    rolled_name = CharacterNames.roll_random(rolled_race, rolled_gender)

    print(f'{rolled_name}')
    print(f'{rolled_gender}')
    print(f'{rolled_race}')
    print(f'{rolled_profession}')


def roll_character(**kwargs):
    """Function docstring."""

    new_kwargs = {}

    gender = kwargs.get('gender')
    if gender:
        new_kwargs['gender'] = CharacterGenders.roll(gender)
    race = kwargs.get('race')
    if race:
        new_kwargs['race'] = CharacterRaces.roll(race)

    npc = RandomNPC(**new_kwargs)

    print(f'{npc.long_description(False)}')


def main():
    """Function docstring."""

    # roll_independently()
    roll_character(**{'race': Races.HALF_ELF})


if __name__ == '__main__':
    main()
