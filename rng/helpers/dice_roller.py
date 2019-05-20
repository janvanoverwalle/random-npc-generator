"""
Module docstring.
"""
import random


class Dice(object):
    """Class docstring."""

    @classmethod
    def roll(cls, dice_to_roll: str):
        """Method docstring."""
        dice_to_roll_list = dice_to_roll.lower().strip().replace(' ', '').split(',')
        outcome = 0
        for dice in dice_to_roll_list:
            dice_data = dice.split('d')
            amount = int(dice_data[0]) if dice_data[0] else 1
            if '+' in dice_data[1]:
                mod_data = dice_data[1].split('+')
                dice_type = int(mod_data[0])
                modifier = int(mod_data[1])
            elif '-' in dice_data[1]:
                mod_data = dice_data[1].split('-')
                dice_type = int(mod_data[0])
                modifier = -int(mod_data[1])
            else:
                dice_type = int(dice_data[1])
                modifier = 0

            total = 0
            for _ in range(amount):
                total += random.randint(1, dice_type)

            outcome += total + modifier
        return outcome
