"""
Module docstring.
"""
from rng.models.names import CharacterNames
from rng.models.professions import CharacterProfessions
from rng.models.races import CharacterRaces
from rng.models.sexes import CharacterSexes


def main():
    """Function docstring."""

    # Sex
    rolled_sex = CharacterSexes.roll_random()

    # Race
    rolled_race = CharacterRaces.roll_random()

    # Profession
    rolled_profession = CharacterProfessions.roll_random('city')

    # Name
    rolled_name = CharacterNames.roll_random(rolled_race, rolled_sex)

    print(f'{rolled_name}')
    print(f'{rolled_sex}')
    print(f'{rolled_race}')
    print(f'{rolled_profession}')


if __name__ == '__main__':
    main()
