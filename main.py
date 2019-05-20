"""
Module docstring.
"""
import random
from rng.helpers.dice_roller import Dice
from rng.models.creature_races import *


def main():
    """Function docstring."""
    available_races = [
        Dragonborn,
        HillDwarf, MountainDwarf,
        HighElf, WoodElf, DarkElf,
        RockGnome, ForestGnome,
        HalfElf,
        HalfOrc,
        LightfootHalfling, StoutHalfling,
        Human,
        Tiefling
    ]
    chosen_race = random.choice(available_races)()
    print(f'{chosen_race}')


if __name__ == '__main__':
    main()
