"""
Module docstring.
"""


class Senses(object):
    """Class docstring."""

    BLINDSIGHT = 'Blindsight'
    DARKVISION = 'Darkvision'
    TREMORSENSE = 'Tremorsense'
    TRUESIGHT = 'Truesight'


class Sense(object):
    """Class docstring."""

    def __init__(self, name, range_in_feet, description=None):
        self.name = name
        self.range = range_in_feet
        self.description = description

    def __str__(self):
        return f'{self.name} ({self.range} ft.)'

    def __repr__(self):
        return str(self)

    def to_json(self):
        return {
            'name': self.name,
            'range': self.range,
            'description': self.description
        }


class Blindsight(Sense):
    """Class docstring."""

    def __init__(self, range_in_feet):
        description = (
            'A monster with blindsight can perceive its surroundings without relying on sight, '
            'within a specific radius.'
            '\n'
            'Creatures without eyes, such as grimlocks and gray oozes, '
            'typically have this special sense, '
            'as do creatures with echolocation or heightened Sense, such as bats and true dragons.'
            '\n'
            'If a monster is naturally blind, it has a parenthetical note to this effect, '
            'indicating that the radius of its blindsight defines the maximum range of its perception.'
        )
        super().__init__(Senses.BLINDSIGHT, range_in_feet, description)


class Darkvision(Sense):
    """Class docstring."""

    def __init__(self, range_in_feet):
        description = (
            'A monster with darkvision can see in the dark within a specific radius. '
            'The monster can see in dim light within the radius as if it were bright light, '
            'and in darkness as if it were dim light.'
            'The monster can\'t discern color in darkness, only shades of gray. '
            'Many creatures that live underground have this special sense.'
        )
        super().__init__(Senses.DARKVISION, range_in_feet, description)


class Tremorsense(Sense):
    """Class docstring."""

    def __init__(self, range_in_feet):
        description = (
            'A monster with tremorsense can detect and pinpoint the origin of vibrations within a specific radius, '
            'provided that the monster and the source of the vibrations are in contact with the same ground or substance.'
            '\n'
            'Tremorsense can\'t be used to detect flying or incorporeal creatures. Many burrowing creatures, '
            'such as ankhegs, have this special sense.'
        )
        super().__init__(Senses.TREMORSENSE, range_in_feet, description)


class Truesight(Sense):
    """Class docstring."""

    def __init__(self, range_in_feet):
        description = (
            'A monster with truesight can, out to a specific range, '
            'see in normal and magical darkness, see invisible creatures and objects, '
            'automatically detect visual illusions and succeed on saving throws against them, '
            'and perceive the original form of a shapechanger or a creature that is transformed by magic. '
            'Furthermore, the monster can see into the Ethereal Plane within the same range.'
        )
        super().__init__(Senses.TRUESIGHT, range_in_feet, description)
