"""
Module docstring.
"""
import random
import numpy
from rng.helpers.dice_roller import Dice
from rng.resources.data.races import Races


class Age(object):
    """Class docstring"""

    _race_to_age_dice_map = {
        Races.DRAGONBORN: ['1d4', '1d6', '2d4'],
        Races.DWARF: ['3d6', '5d6', '7d6'],
        Races.ELF: ['4d6', '6d6', '10d6'],
        Races.GNOME: ['4d6', '6d6', '9d6'],
        Races.HALF_ELF: ['1d6', '2d6', '3d6'],
        Races.HALF_ORC: ['1d4', '1d6', '2d6'],
        Races.HALFLING: ['2d4', '3d6', '4d6'],
        Races.HUMAN: ['1d4', '1d6', '2d6'],
        Races.TIEFLING: ['1d4', '1d6', '2d6']
    }

    _age_description_map = {
        'a child': range(0, 12),
        'a teenager': range(12, 17),
        'a young adult': range(18, 30),
        'an adult': range(30, 45),
        'middle-aged': range(45, 65),
        'a senior': range(65, 75),
        'elderly': range(75, 100)
    }

    def __init__(self, lifespan, physical, mental=None, current=None):
        self.lifespan = lifespan
        self.physical_maturation = physical
        self.mental_maturation = mental if mental else physical
        self.current = current
        self.expected_lifespan = None
        self.adulthood = max(self.physical_maturation, self.mental_maturation)

    def __str__(self):
        if self.current:
            info = f'Expected lifespan: {self.expected_lifespan}, Adulthood: {self.adulthood}'
            return f'{self.current} years old ({info}, Human Equivalent: ~{self.human_equivalent})'

        if isinstance(self.lifespan, (tuple, list)):
            lifespan = f'Between {self.lifespan[0]} and {self.lifespan[1]}'
        else:
            lifespan = self.lifespan
        return f'Expected lifespan: {lifespan}, Adulthood: {self.adulthood}'

    @property
    def human_equivalent(self):
        """Method docstring."""
        return int((self.current/self.expected_lifespan)*80)

    def age_description(self):
        """Method docstring."""
        human_eq = self.human_equivalent
        for k, v in self._age_description_map.items():
            if human_eq in v:
                return k
        return random.choice(['weird', '...a person?', 'a carrot'])

    def roll_random(self, race, char_class=None):
        """Method docstring."""
        if isinstance(self.lifespan, (tuple, list)):
            lifespan = int(random.uniform(self.lifespan[0], self.lifespan[1]))
        else:
            lifespan = self.lifespan
        self.expected_lifespan = int(lifespan * random.uniform(0.95, 1.05))

        die_list = self._race_to_age_dice_map.get(Races.get_base_race(race.name))

        if char_class:
            pass  # TODO: Take class into account
        else:
            die = random.choice(die_list)

        age = int((self.adulthood + Dice.roll(die, max=True)) * numpy.random.normal(2.2, 0.75))
        if age > (self.expected_lifespan * 1.1):
            age = int(self.expected_lifespan * random.uniform(1, 1.1))
        self.current = age
        return self.current
