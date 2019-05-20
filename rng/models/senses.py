"""
Module docstring.
"""


class Sense(object):
    """Class docstring."""

    def __init__(self, name, range_in_feet, description=None):
        self.name = name
        self.range = range_in_feet
        self.description = description

    def __str__(self):
        return f'{self.name} ({self.range} ft.)'


class Darkvision(Sense):
    """Class docstring."""

    def __init__(self, range_in_feet):
        super().__init__('Darkvision', range_in_feet)
