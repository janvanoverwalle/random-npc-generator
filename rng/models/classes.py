"""
Module docstring.
"""
import random
from rng.resources.data.abilities import Abilities
from rng.resources.data.classes import Classes
from rng.resources.data.strings import Strings


class CharacterClasses(object):
    """Class docstring."""

    _name_to_class_map = None

    @classmethod
    def get(cls, class_name):
        """Method docstring."""
        if not cls._name_to_class_map:
            cls._name_to_class_map = {
                Classes.BARBARIAN: Barbarian,
                Classes.BARD: Bard,
                Classes.CLERIC: Cleric,
                Classes.DRUID: Druid,
                Classes.FIGHTER: Fighter,
                Classes.MONK: Monk,
                Classes.PALADIN: Paladin,
                Classes.RANGER: Ranger,
                Classes.ROGUE: Rogue,
                Classes.SORCERER: Sorcerer,
                Classes.WARLOCK: Warlock,
                Classes.WIZARD: Wizard,
            }

        if not isinstance(class_name, (list, tuple)):
            class_name = [class_name]

        classes = []
        for name in class_name:
            if not name or Strings.equals_ignore_case(name, Strings.RANDOM):
                classes += [v for k, v in cls._name_to_class_map.items() if v not in classes]
            else:
                name = cls._name_to_class_map.get(name)
                if name not in classes:
                    classes.append(name)
        return classes

    @classmethod
    def roll(cls, class_name=None, amount=1):
        """Method docstring."""
        if not amount:
            return None

        available_classes = cls.get(class_name)

        results = [random.choice(c)() if isinstance(c, list) else c() for c in random.choices(available_classes, k=amount)]
        return results[0] if amount == 1 else results

    @classmethod
    def roll_random(cls, amount=1):
        """Method docstring."""
        return cls.roll(Strings.RANDOM, amount)


class CharacterClass(object):
    """Class docstring."""

    def __init__(self, class_name):
        self._name = class_name
        self._subclasses = Classes.subclasses_as_list(self.name)
        self._hit_die = None
        self._primary_abilities = None
        self._saving_throws = None

    def __str__(self):
        return self._name

    @property
    def name(self):
        """Method docstring."""
        return self._name

    @property
    def subclasses(self):
        """Method docstring."""
        return self._subclasses

    @property
    def hit_die(self):
        """Method docstring."""
        return self._hit_die

    @hit_die.setter
    def hit_die(self, value):
        """Method docstring."""
        digits = [c for c in str(value).strip() if c.isdigit()]
        self._hit_die = 'd' + ''.join(digits)

    @property
    def primary_abilities(self):
        """Method docstring."""
        return self._primary_abilities

    @property
    def saving_throws(self):
        """Method docstring."""
        return self._saving_throws

    def info_string(self):
        """Method docstring."""
        return str(self)


class Barbarian(CharacterClass):
    """Class docstring."""

    def __init__(self):
        super().__init__(Classes.BARBARIAN)
        self.hit_die = 12
        self._primary_abilities = [Abilities.STRENGTH]
        self._saving_throws = [
            Abilities.STRENGTH,
            Abilities.CONSTITUTION
        ]


class Bard(CharacterClass):
    """Class docstring."""

    def __init__(self):
        super().__init__(Classes.BARD)
        self.hit_die = 8
        self._primary_abilities = [Abilities.CHARISMA]
        self._saving_throws = [
            Abilities.DEXTERITY,
            Abilities.CHARISMA
        ]


class Cleric(CharacterClass):
    """Class docstring."""

    def __init__(self):
        super().__init__(Classes.CLERIC)
        self.hit_die = 8
        self._primary_abilities = [Abilities.WISDOM]
        self._saving_throws = [
            Abilities.WISDOM,
            Abilities.CHARISMA
        ]


class Druid(CharacterClass):
    """Class docstring."""

    def __init__(self):
        super().__init__(Classes.DRUID)
        self.hit_die = 8
        self._primary_abilities = [Abilities.WISDOM]
        self._saving_throws = [
            Abilities.INTELLIGENCE,
            Abilities.WISDOM
        ]


class Fighter(CharacterClass):
    """Class docstring."""

    def __init__(self, primary_ability=None):
        super().__init__(Classes.FIGHTER)
        self.hit_die = 10
        if primary_ability:
            self._primary_abilities = [Abilities.convert(primary_ability)]
        else:
            self._primary_abilities = [random.choice([Abilities.STRENGTH, Abilities.DEXTERITY])]
        self._saving_throws = [
            Abilities.STRENGTH,
            Abilities.CONSTITUTION
        ]


class Monk(CharacterClass):
    """Class docstring."""

    def __init__(self):
        super().__init__(Classes.MONK)
        self.hit_die = 8
        self._primary_abilities = [
            Abilities.DEXTERITY,
            Abilities.WISDOM
        ]
        self._saving_throws = [
            Abilities.STRENGTH,
            Abilities.DEXTERITY
        ]


class Paladin(CharacterClass):
    """Class docstring."""

    def __init__(self):
        super().__init__(Classes.PALADIN)
        self.hit_die = 10
        self._primary_abilities = [
            Abilities.STRENGTH,
            Abilities.CHARISMA
        ]
        self._saving_throws = [
            Abilities.WISDOM,
            Abilities.CHARISMA
        ]


class Ranger(CharacterClass):
    """Class docstring."""

    def __init__(self):
        super().__init__(Classes.RANGER)
        self.hit_die = 10
        self._primary_abilities = [
            Abilities.DEXTERITY,
            Abilities.WISDOM
        ]
        self._saving_throws = [
            Abilities.STRENGTH,
            Abilities.DEXTERITY
        ]


class Rogue(CharacterClass):
    """Class docstring."""

    def __init__(self):
        super().__init__(Classes.ROGUE)
        self.hit_die = 8
        self._primary_abilities = [Abilities.DEXTERITY]
        self._saving_throws = [
            Abilities.DEXTERITY,
            Abilities.INTELLIGENCE
        ]


class Sorcerer(CharacterClass):
    """Class docstring."""

    def __init__(self):
        super().__init__(Classes.SORCERER)
        self.hit_die = 6
        self._primary_abilities = [Abilities.CHARISMA]
        self._saving_throws = [
            Abilities.CONSTITUTION,
            Abilities.CHARISMA
        ]


class Warlock(CharacterClass):
    """Class docstring."""

    def __init__(self):
        super().__init__(Classes.WARLOCK)
        self.hit_die = 8
        self._primary_abilities = [Abilities.CHARISMA]
        self._saving_throws = [
            Abilities.WISDOM,
            Abilities.CHARISMA
        ]


class Wizard(CharacterClass):
    """Class docstring."""

    def __init__(self):
        super().__init__(Classes.WIZARD)
        self.hit_die = 6
        self._primary_abilities = [Abilities.INTELLIGENCE]
        self._saving_throws = [
            Abilities.WISDOM,
            Abilities.INTELLIGENCE
        ]
