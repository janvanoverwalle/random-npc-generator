"""
Module docstring.
"""
from rng.models.abilities import Abilities
from rng.models.languages import Languages
from rng.models.skills import Skills
from rng.models.sizes import CreatureSize
from rng.models.ages import CreatureAge
from rng.models.senses import Darkvision


class Races(object):
    """ Class docstring."""

    DRAGONBORN = 'dragoborn'
    DWARF = 'dwarf'
    HILL_DWARF = 'hill dwarf'
    MOUNTAIN_DWARF = 'mountain dwarf'
    ELF = 'elf'
    HIGH_ELF = 'high elf'
    WOOD_ELF = 'wood elf'
    DARK_ELF = 'dark elf'
    GNOME = 'gnome'
    ROCK_GNOME = 'rock gnome'
    FOREST_GNOME = 'forest gnome'
    HALF_ELF = 'half-elf'
    HALF_ORC = 'half-orc'
    HALFLING = 'halfling'
    LIGHTFOOT_HALFLING = 'lightfoot halfling'
    STOUT_HALFLING = 'stout halfling'
    HUMAN = 'human'
    TIEFLING = 'tiefling'


class CreatureRace(object):
    """Class docstring."""

    def __init__(self, race):
        self.race = race
        self.size = CreatureSize.NONE
        self.speed = 0
        self.age = None
        self.ability_score_increases = None
        self.languages = None
        self.senses = None
        self.skills = None

    def __str__(self):
        tab = '\t'
        newline = '\n'
        string = f'Race: {self.race}{newline}'
        string += f'Size: {self.size}{newline}'
        string += f'Speed: {self.speed}{newline}'
        string += f'Age: {self.age}{newline}'
        if self.ability_score_increases:
            string += f'Ability Score Increases:{newline}'
            for elem in self.ability_score_increases:
                string += f'{tab}{elem[0]}: {elem[1]}{newline}'
        if self.senses:
            string += f'Senses:{newline}'
            for elem in self.senses:
                string += f'{tab}{elem}{newline}'
        if self.languages:
            string += f'Languages:{newline}'
            for elem in self.languages:
                string += f'{tab}{elem}{newline}'
        if self.skills:
            string += f'Skills:{newline}'
            for elem in self.skills:
                string += f'{tab}{elem}{newline}'
        return string


class Dragonborn(CreatureRace):
    """Class docstring."""

    def __init__(self):
        super().__init__(Races.DRAGONBORN)
        self.ability_score_increases = [
            (Abilities.STRENGTH, 2),
            (Abilities.CHARISMA, 1)
        ]
        self.age = CreatureAge(80, 3, 15)
        self.size = CreatureSize.MEDIUM
        self.speed = 30
        self.languages = [
            Languages.COMMON,
            Languages.DRACONIC
        ]


class Dwarf(CreatureRace):
    """Class docstring."""

    def __init__(self, race=None):
        super().__init__(race if race else Races.DWARF)
        self.ability_score_increases = [
            (Abilities.CONSTITUTION, 2)
        ]
        self.age = CreatureAge(350, 20, 50)
        self.size = CreatureSize.MEDIUM
        self.speed = 25
        self.languages = [
            Languages.COMMON,
            Languages.DWARVISH
        ]
        self.senses = [
            Darkvision(60)
        ]


class HillDwarf(Dwarf):
    """Class docstring."""

    def __init__(self):
        super().__init__(Races.HILL_DWARF)
        self.ability_score_increases.append((Abilities.WISDOM, 1))


class MountainDwarf(Dwarf):
    """Class docstring."""

    def __init__(self):
        super().__init__(Races.MOUNTAIN_DWARF)
        self.ability_score_increases.append((Abilities.STRENGTH, 2))


class Elf(CreatureRace):
    """Class docstring."""

    def __init__(self, race=None):
        super().__init__(race if race else Races.ELF)
        self.ability_score_increases = [
            (Abilities.DEXTERITY, 2)
        ]
        self.age = CreatureAge(750, 20, 100)
        self.size = CreatureSize.MEDIUM
        self.speed = 30
        self.languages = [
            Languages.COMMON,
            Languages.ELVISH
        ]
        self.senses = [
            Darkvision(60)
        ]
        self.skills = [
            Skills.PERCEPTION
        ]


class HighElf(Elf):
    """Class docstring."""

    def __init__(self):
        super().__init__(Races.HIGH_ELF)
        self.ability_score_increases.append((Abilities.INTELLIGENCE, 1))


class WoodElf(Elf):
    """Class docstring."""

    def __init__(self):
        super().__init__(Races.WOOD_ELF)
        self.ability_score_increases.append((Abilities.WISDOM, 1))
        self.speed = 35


class DarkElf(Elf):
    """Class docstring."""

    def __init__(self):
        super().__init__(Races.DARK_ELF)
        #self.ability_score_increases.append((Abilities.?, ?))


class Gnome(CreatureRace):
    """Class docstring."""

    def __init__(self, race=None):
        super().__init__(race if race else Races.GNOME)
        self.ability_score_increases = [
            (Abilities.INTELLIGENCE, 2)
        ]
        self.age = CreatureAge((350, 500), 40, 40)
        self.size = CreatureSize.SMALL
        self.speed = 25
        self.languages = [
            Languages.COMMON,
            Languages.GNOMISH
        ]
        self.senses = [
            Darkvision(60)
        ]


class RockGnome(Gnome):
    """Class docstring."""

    def __init__(self):
        super().__init__(Races.ROCK_GNOME)
        self.ability_score_increases.append((Abilities.CONSTITUTION, 1))


class ForestGnome(Gnome):
    """Class docstring."""

    def __init__(self):
        super().__init__(Races.FOREST_GNOME)
        # self.ability_score_increases.append((Abilities.?, ?))


class HalfElf(CreatureRace):
    """Class docstring."""

    def __init__(self, race=None):
        super().__init__(race if race else Races.HALF_ELF)
        self.ability_score_increases = [
            (Abilities.CHARISMA, 2),
            ('random', 1),
            ('random', 1)
        ]
        self.age = CreatureAge(180, 20, 20)
        self.size = CreatureSize.MEDIUM
        self.speed = 30
        self.languages = [
            Languages.COMMON,
            Languages.ELVISH,
            'random'
        ]
        self.senses = [
            Darkvision(60)
        ]
        self.skills = [
            'random',
            'random'
        ]


class HalfOrc(CreatureRace):
    """Class docstring."""

    def __init__(self, race=None):
        super().__init__(race if race else Races.HALF_ORC)
        self.ability_score_increases = [
            (Abilities.STRENGTH, 2),
            (Abilities.CONSTITUTION, 1)
        ]
        self.age = CreatureAge(75, 14, 14)
        self.size = CreatureSize.MEDIUM
        self.speed = 30
        self.languages = [
            Languages.COMMON,
            Languages.ORCISH
        ]
        self.senses = [
            Darkvision(60)
        ]
        self.skills = [
            Skills.INTIMIDATION
        ]


class Halfling(CreatureRace):
    """Class docstring."""

    def __init__(self, race=None):
        super().__init__(race if race else Races.HALFLING)
        self.ability_score_increases = [
            (Abilities.DEXTERITY, 2)
        ]
        self.age = CreatureAge(150, 20, 20)
        self.size = CreatureSize.SMALL
        self.speed = 25
        self.languages = [
            Languages.COMMON,
            Languages.HALFLING
        ]


class LightfootHalfling(Halfling):
    """Class docstring."""

    def __init__(self):
        super().__init__(Races.LIGHTFOOT_HALFLING)
        self.ability_score_increases.append((Abilities.CHARISMA, 1))


class StoutHalfling(Halfling):
    """Class docstring."""

    def __init__(self):
        super().__init__(Races.STOUT_HALFLING)
        self.ability_score_increases.append((Abilities.CONSTITUTION, 1))


class Human(CreatureRace):
    """Class docstring."""

    def __init__(self, race=None):
        super().__init__(race if race else Races.HUMAN)
        self.ability_score_increases = [
            (Abilities.STRENGTH, 1),
            (Abilities.DEXTERITY, 1),
            (Abilities.CONSTITUTION, 1),
            (Abilities.INTELLIGENCE, 1),
            (Abilities.WISDOM, 1),
            (Abilities.CHARISMA, 1)
        ]
        self.age = CreatureAge(85, 20, 20)
        self.size = CreatureSize.MEDIUM
        self.speed = 30
        self.languages = [
            Languages.COMMON,
            'random'
        ]


class VariantHuman(Human):
    """Class docstring."""

    def __init__(self, race=None):
        super().__init__(race if race else Races.HUMAN)
        self.ability_score_increases = [
            ('random', 1),
            ('random', 1)
        ]
        self.skills = [
            'random'
        ]
        self.feats = [
            'random'
        ]
