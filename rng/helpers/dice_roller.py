"""
Module docstring.
"""
import random


class Dice(object):
    """Class docstring."""

    @classmethod
    def roll(cls, dice_to_roll: str, **kwargs):
        """Method docstring."""
        if isinstance(dice_to_roll, str):
            dice_to_roll_list = dice_to_roll.lower().strip().replace(' ', '').split(',')
        else:
            try:
                int(dice_to_roll)
                dice_to_roll = str(dice_to_roll)
            except ValueError:
                pass
            try:
                _ = dice_to_roll[0]
            except TypeError:
                dice_to_roll = [dice_to_roll]
            dice_to_roll_list = dice_to_roll

        outcome = 0
        for dice in dice_to_roll_list:
            try:
                int(dice)
                dice = f'd{dice}'
            except ValueError:
                pass
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
                if kwargs.get('max'):
                    total += dice_type
                elif kwargs.get('min'):
                    total += 1
                else:
                    total += random.randint(1, dice_type)

            outcome += total + modifier
        return outcome
