"""
Module docstring.
"""
from rng.models.races import Races
from rng.helpers.dice_roller import Dice


class CreatureAge(object):
    """Class docstring"""

    def __init__(self, lifespan, physical, mental, current=None):
        self.lifespan = lifespan  # Could be a tuple indicating a range
        self.physical_maturation = physical
        self.mental_maturation = mental
        self.current = current
        self.adulthood = max(self.physical_maturation, self.mental_maturation)

    def __str__(self):
        return f'Lifespan: {self.lifespan}, Adulthood: {self.adulthood}'

    def roll_age(self, creature_race, creature_class=None):
        """Method docstring"""
        dice_to_roll = '1d4'
        if creature_race.race == Races.DRAGONBORN:
            dice_to_roll = '1d4'
        return self.adulthood + Dice.roll(dice_to_roll)
