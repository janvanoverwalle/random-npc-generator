"""
Module docstring.
"""
import random
from rng.models.ages import Age
from rng.models.senses import Darkvision
from rng.resources.objects.abilities import Abilities
from rng.resources.objects.languages import Languages
from rng.resources.objects.sizes import Size
from rng.resources.objects.skills import Skills
from rng.resources.objects.strings import Strings


class CharacterRaces(object):
    """Class docstring."""

    DRAGONBORN = 'Dragonborn'
    DWARF = 'Dwarf'
    HILL_DWARF = f'Hill {DWARF}'
    MOUNTAIN_DWARF = f'Mountain {DWARF}'
    ELF = 'Elf'
    HIGH_ELF = f'High {ELF}'
    WOOD_ELF = f'Wood {ELF}'
    DARK_ELF = f'Dark {ELF}'
    GNOME = 'Gnome'
    ROCK_GNOME = f'Rock {GNOME}'
    FOREST_GNOME = f'Forest {GNOME}'
    HALF_ELF = 'Half-elf'
    HALF_ORC = 'Half-orc'
    HALFLING = 'Halfling'
    LIGHTFOOT_HALFLING = f'Lightfoot {HALFLING}'
    STOUT_HALFLING = f'Stout {HALFLING}'
    HUMAN = 'Human'
    TIEFLING = 'Tiefling'

    @classmethod
    def as_list(cls):
        """Method docstring."""
        return [
            cls.DRAGONBORN,
            cls.HILL_DWARF,
            cls.MOUNTAIN_DWARF,
            cls.HIGH_ELF,
            cls.WOOD_ELF,
            cls.DARK_ELF,
            cls.ROCK_GNOME,
            cls.FOREST_GNOME,
            cls.HALF_ELF,
            cls.HALF_ORC,
            cls.LIGHTFOOT_HALFLING,
            cls.STOUT_HALFLING,
            cls.HUMAN,
            cls.TIEFLING,
        ]

    @classmethod
    def roll_random(cls, amount=1):
        """Method docstring."""

        if not amount:
            return None

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
        results = [c() for c in random.choices(available_races, k=amount)]
        return results[0] if amount == 1 else results


class CharacterRace(object):
    """Class docstring."""

    def __init__(self, name):
        self._basic_rules = True

        self.name = name
        self.size = Size.NONE
        self.speed = 0
        self.age = None
        self.ability_score_increases = []
        self.languages = []
        self.senses = []
        self.skills = []

    def __str__(self):
        string = f'Race: {self.name}{Strings.NEWLINE}'
        string += f'Size: {self.size}{Strings.NEWLINE}'
        string += f'Speed: {self.speed} ft.{Strings.NEWLINE}'
        string += f'Age: {self.age}{Strings.NEWLINE}'
        if self.ability_score_increases:
            string += f'Ability Score Increases:{Strings.NEWLINE}'
            for elem in self.ability_score_increases:
                string += f'{Strings.TAB}{elem[0]}: {elem[1]}{Strings.NEWLINE}'
        if self.senses:
            string += f'Senses:{Strings.NEWLINE}'
            for elem in self.senses:
                string += f'{Strings.TAB}{elem}{Strings.NEWLINE}'
        if self.languages:
            string += f'Languages:{Strings.NEWLINE}'
            for elem in self.languages:
                string += f'{Strings.TAB}{elem}{Strings.NEWLINE}'
        if self.skills:
            string += f'Skills:{Strings.NEWLINE}'
            for elem in self.skills:
                string += f'{Strings.TAB}{elem}{Strings.NEWLINE}'
        return string[:-1]  # Strip the last newline

    def _parse_random_ability_score_increases(self):
        if not self.ability_score_increases:
            return

        abilities = Abilities.as_list()
        for ability in self.ability_score_increases:
            if ability[0] not in abilities:
                continue
            abilities.remove(ability[0])

        for index, ability in enumerate(self.ability_score_increases):
            if ability[0] != Strings.RANDOM:
                continue
            random_ability = abilities.pop(random.randint(1, len(abilities)-1))
            self.ability_score_increases[index] = (random_ability, ability[1])

    def _parse_random_languages(self):
        if not self.languages:
            return

        standard_languages = [l for l in Languages.standard_as_list() if l not in self.languages]
        exotic_languages = [l for l in Languages.exotic_as_list() if l not in self.languages]

        """
        languages = Languages.as_list()
        for language in self.languages:
            if language not in languages:
                continue
            languages.remove(language)
        """

        for index, language in enumerate(self.languages):
            if language != Strings.RANDOM:
                continue
            exotic_chance = random.randint(1, 100)
            language_list = exotic_languages if exotic_chance <= 10 else standard_languages
            random_language = language_list.pop(random.randint(1, len(language_list)-1))
            self.languages[index] = random_language

    def _parse_random_skills(self):
        if not self.skills:
            return

        skills = Skills.as_list()
        for skill in self.skills:
            if skill not in skills:
                continue
            skills.remove(skill)

        for index, skill in enumerate(self.skills):
            if skill != Strings.RANDOM:
                continue

            random_skill = skills.pop(random.randint(1, len(skills)-1))
            self.skills[index] = random_skill

    def _parse_random_abilities(self):
        self._parse_random_ability_score_increases()
        self._parse_random_languages()
        self._parse_random_skills()


class Dragonborn(CharacterRace):
    """Class docstring."""

    def __init__(self):
        super().__init__(CharacterRaces.DRAGONBORN)
        self.ability_score_increases = [
            (Abilities.STRENGTH, 2),
            (Abilities.CHARISMA, 1)
        ]
        self.age = Age(80, 3, 15)
        self.size = Size.MEDIUM
        self.speed = 30
        self.languages = [
            Languages.COMMON,
            Languages.DRACONIC
        ]


class Dwarf(CharacterRace):
    """Class docstring."""

    def __init__(self, race=None):
        super().__init__(race if race else CharacterRaces.DWARF)
        self.ability_score_increases = [
            (Abilities.CONSTITUTION, 2)
        ]
        self.age = Age(350, 20, 50)
        self.size = Size.MEDIUM
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
        super().__init__(CharacterRaces.HILL_DWARF)
        self.ability_score_increases.append((Abilities.WISDOM, 1))


class MountainDwarf(Dwarf):
    """Class docstring."""

    def __init__(self):
        super().__init__(CharacterRaces.MOUNTAIN_DWARF)
        self.ability_score_increases.append((Abilities.STRENGTH, 2))


class Elf(CharacterRace):
    """Class docstring."""

    def __init__(self, race=None):
        super().__init__(race if race else CharacterRaces.ELF)
        self.ability_score_increases = [
            (Abilities.DEXTERITY, 2)
        ]
        self.age = Age(750, 20, 100)
        self.size = Size.MEDIUM
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
        super().__init__(CharacterRaces.HIGH_ELF)
        self.ability_score_increases.append((Abilities.INTELLIGENCE, 1))


class WoodElf(Elf):
    """Class docstring."""

    def __init__(self):
        super().__init__(CharacterRaces.WOOD_ELF)
        self.ability_score_increases.append((Abilities.WISDOM, 1))
        self.speed = 35


class DarkElf(Elf):
    """Class docstring."""

    def __init__(self):
        super().__init__(CharacterRaces.DARK_ELF)
        self._basic_rules = False

        self.ability_score_increases.append((Abilities.CHARISMA, 1))
        self.senses = [
            Darkvision(120)
        ]


class Gnome(CharacterRace):
    """Class docstring."""

    def __init__(self, race=None):
        super().__init__(race if race else CharacterRaces.GNOME)
        self.ability_score_increases = [
            (Abilities.INTELLIGENCE, 2)
        ]
        self.age = Age((350, 500), 40, 40)
        self.size = Size.SMALL
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
        super().__init__(CharacterRaces.ROCK_GNOME)
        self.ability_score_increases.append((Abilities.CONSTITUTION, 1))


class ForestGnome(Gnome):
    """Class docstring."""

    def __init__(self):
        super().__init__(CharacterRaces.FOREST_GNOME)
        self._basic_rules = False

        self.ability_score_increases.append((Abilities.DEXTERITY, 1))


class HalfElf(CharacterRace):
    """Class docstring."""

    def __init__(self, race=None):
        super().__init__(race if race else CharacterRaces.HALF_ELF)

        self.age = Age(180, 20, 20)
        self.size = Size.MEDIUM
        self.speed = 30
        self.ability_score_increases = [
            (Abilities.CHARISMA, 2),
            (Strings.RANDOM, 1),
            (Strings.RANDOM, 1)
        ]
        self.languages = [
            Languages.COMMON,
            Languages.ELVISH,
            Strings.RANDOM
        ]
        self.senses = [
            Darkvision(60)
        ]
        self.skills = [
            Strings.RANDOM,
            Strings.RANDOM
        ]
        # self._parse_random_abilities()


class HalfOrc(CharacterRace):
    """Class docstring."""

    def __init__(self, race=None):
        super().__init__(race if race else CharacterRaces.HALF_ORC)
        self.ability_score_increases = [
            (Abilities.STRENGTH, 2),
            (Abilities.CONSTITUTION, 1)
        ]
        self.age = Age(75, 14, 14)
        self.size = Size.MEDIUM
        self.speed = 30
        self.languages = [
            Languages.COMMON,
            Languages.ORC
        ]
        self.senses = [
            Darkvision(60)
        ]
        self.skills = [
            Skills.INTIMIDATION
        ]


class Halfling(CharacterRace):
    """Class docstring."""

    def __init__(self, race=None):
        super().__init__(race if race else CharacterRaces.HALFLING)
        self.ability_score_increases = [
            (Abilities.DEXTERITY, 2)
        ]
        self.age = Age(150, 20, 20)
        self.size = Size.SMALL
        self.speed = 25
        self.languages = [
            Languages.COMMON,
            Languages.HALFLING
        ]


class LightfootHalfling(Halfling):
    """Class docstring."""

    def __init__(self):
        super().__init__(CharacterRaces.LIGHTFOOT_HALFLING)
        self.ability_score_increases.append((Abilities.CHARISMA, 1))


class StoutHalfling(Halfling):
    """Class docstring."""

    def __init__(self):
        super().__init__(CharacterRaces.STOUT_HALFLING)
        self.ability_score_increases.append((Abilities.CONSTITUTION, 1))


class Human(CharacterRace):
    """Class docstring."""

    def __init__(self, race=None):
        super().__init__(race if race else CharacterRaces.HUMAN)
        self.ability_score_increases = [
            (Abilities.STRENGTH, 1),
            (Abilities.DEXTERITY, 1),
            (Abilities.CONSTITUTION, 1),
            (Abilities.INTELLIGENCE, 1),
            (Abilities.WISDOM, 1),
            (Abilities.CHARISMA, 1)
        ]
        self.age = Age(85, 20, 20)
        self.size = Size.MEDIUM
        self.speed = 30
        self.languages = [
            Languages.COMMON,
            Strings.RANDOM
        ]
        # self._parse_random_abilities()


class VariantHuman(Human):
    """Class docstring."""

    def __init__(self, race=None):
        super().__init__(race if race else CharacterRaces.HUMAN)
        self.ability_score_increases = [
            (Strings.RANDOM, 1),
            (Strings.RANDOM, 1)
        ]
        self.skills = [
            Strings.RANDOM
        ]
        self.feats = [
            Strings.RANDOM
        ]
        # self._parse_random_abilities()


class Tiefling(CharacterRace):
    """Class docstring."""

    def __init__(self, race=None):
        super().__init__(race if race else CharacterRaces.TIEFLING)
        self.ability_score_increases = [
            (Abilities.INTELLIGENCE, 1),
            (Abilities.CHARISMA, 2)
        ]
        self.age = Age(90, 20, 20)
        self.size = Size.MEDIUM
        self.speed = 30
        self.languages = [
            Languages.COMMON,
            Languages.INFERNAL
        ]
        self.senses = [
            Darkvision(60)
        ]
