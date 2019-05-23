"""
Module docstring.
"""
from rng.models.characters import RandomNPC
from rng.models.names import CharacterNames
from rng.models.professions import CharacterProfessions
from rng.models.races import CharacterRaces
from rng.models.genders import CharacterGenders


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


def roll_character():
    """Function docstring."""

    npc = RandomNPC()

    print(f'{npc.long_description()}')
    # print(f'{npc.race.name}: {npc.skills}')


def main():
    """Function docstring."""

    # roll_independently()
    roll_character()


if __name__ == '__main__':
    main()
