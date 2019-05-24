"""
Module docstring.
"""
import random
from rng.models.ages import Age
from rng.models.senses import Darkvision
from rng.resources.data.abilities import Abilities
from rng.resources.data.languages import Languages
from rng.resources.data.races import Races
from rng.resources.data.sizes import Sizes
from rng.resources.data.skills import Skills
from rng.resources.data.strings import Strings


class CharacterRaces(object):
    """Class docstring."""

    @classmethod
    def roll(cls, race_name=None, amount=1):
        """Method docstring."""

        if not amount:
            return None

        name_to_race_map = {
            Races.DRAGONBORN: Dragonborn,
            Races.DWARF: [HillDwarf, MountainDwarf],
            Races.HILL_DWARF: HillDwarf,
            Races.MOUNTAIN_DWARF: MountainDwarf,
            Races.ELF: [HighElf, WoodElf, DarkElf],
            Races.HIGH_ELF: HighElf,
            Races.WOOD_ELF: WoodElf,
            Races.DARK_ELF: DarkElf,
            Races.GNOME: [RockGnome, ForestGnome],
            Races.ROCK_GNOME: RockGnome,
            Races.FOREST_GNOME: ForestGnome,
            Races.HALF_ELF: HalfElf,
            Races.HALF_ORC: HalfOrc,
            Races.HALFLING: [LightfootHalfling, StoutHalfling],
            Races.LIGHTFOOT_HALFLING: LightfootHalfling,
            Races.STOUT_HALFLING: StoutHalfling,
            Races.HUMAN: Human,
            Races.TIEFLING: Tiefling
        }

        if not race_name or Strings.equals_ignore_case(race_name, Strings.RANDOM):
            available_races = [v for k, v in name_to_race_map.items()]
        else:
            available_races = [name_to_race_map[race_name]]

        results = [random.choice(c)() if isinstance(c, list) else c() for c in random.choices(available_races, k=amount)]
        return results[0] if amount == 1 else results

    @classmethod
    def roll_random(cls, amount=1):
        """Method docstring."""

        if not amount:
            return None

        return cls.roll(Strings.RANDOM, amount)


class CharacterRace(object):
    """Class docstring."""

    def __init__(self, name):
        self._basic_rules = True

        self.name = name
        self.size = Sizes.NONE
        self.speed = 0
        self.age = None
        self.ability_score_increases = []
        self._original_ability_score_increases = None
        self.languages = []
        self._original_languages = None
        self.senses = []
        self.skills = []
        self._original_skills = None

    def __str__(self):
        string = f'Race: {self.name}{Strings.LF}'
        string += f'  Sizes: {self.size}{Strings.LF}'
        string += f'  Speed: {self.speed} ft.{Strings.LF}'
        string += f'  Age: {self.age}{Strings.LF}'
        if self.ability_score_increases:
            string += f'  Ability Score Increases:{Strings.LF}'
            for elem in self.ability_score_increases:
                string += f'    {elem[0]}: {elem[1]}{Strings.LF}'
        if self.senses:
            string += f'  Senses:{Strings.LF}'
            for elem in self.senses:
                string += f'    {elem}{Strings.LF}'
        if self.languages:
            string += f'  Languages:{Strings.LF}'
            for elem in self.languages:
                string += f'    {elem}{Strings.LF}'
        if self.skills:
            string += f'  Skills:{Strings.LF}'
            for elem in self.skills:
                string += f'    {elem}{Strings.LF}'
        return string.strip()

    def _parse_random_ability_score_increases(self):
        if not self.ability_score_increases:
            return

        if self._original_ability_score_increases is None:
            self._original_ability_score_increases = self.ability_score_increases[:]
        else:
            self.ability_score_increases = self._original_ability_score_increases[:]

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

        if self._original_languages is None:
            self._original_languages = self.languages[:]
        else:
            self.languages = self._original_languages[:]

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

        if self._original_skills is None:
            self._original_skills = self.skills[:]
        else:
            self.skills = self._original_skills[:]

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

    def roll_random_ability_score_increases(self):
        """Method docstring."""
        self._parse_random_ability_score_increases()

    def roll_random_languages(self):
        """Method docstring."""
        self._parse_random_languages()

    def roll_random_skills(self):
        """Method docstring."""
        self._parse_random_skills()

    def roll_random_abilities(self):
        """Method docstring."""
        self.roll_random_ability_score_increases()
        self.roll_random_languages()
        self.roll_random_skills()

    def roll_age(self, char_class=None):
        """Method docstring."""
        return self.age.roll_random(self, char_class)


class Dragonborn(CharacterRace):
    """Class docstring."""

    def __init__(self):
        super().__init__(Races.DRAGONBORN)
        self.ability_score_increases = [
            (Abilities.STRENGTH, 2),
            (Abilities.CHARISMA, 1)
        ]
        self.age = Age(80, 3, 15)
        self.size = Sizes.MEDIUM
        self.speed = 30
        self.languages = [
            Languages.COMMON,
            Languages.DRACONIC
        ]


class Dwarf(CharacterRace):
    """Class docstring."""

    def __init__(self, race=None):
        super().__init__(race if race else Races.DWARF)
        self.ability_score_increases = [
            (Abilities.CONSTITUTION, 2)
        ]
        self.age = Age(350, 20, 50)
        self.size = Sizes.MEDIUM
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


class Elf(CharacterRace):
    """Class docstring."""

    def __init__(self, race=None):
        super().__init__(race if race else Races.ELF)
        self.ability_score_increases = [
            (Abilities.DEXTERITY, 2)
        ]
        self.age = Age(750, 20, 100)
        self.size = Sizes.MEDIUM
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
        self._basic_rules = False

        self.ability_score_increases.append((Abilities.CHARISMA, 1))
        self.senses = [
            Darkvision(120)
        ]


class Gnome(CharacterRace):
    """Class docstring."""

    def __init__(self, race=None):
        super().__init__(race if race else Races.GNOME)
        self.ability_score_increases = [
            (Abilities.INTELLIGENCE, 2)
        ]
        self.age = Age((350, 500), 40)
        self.size = Sizes.SMALL
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
        self._basic_rules = False

        self.ability_score_increases.append((Abilities.DEXTERITY, 1))


class HalfElf(CharacterRace):
    """Class docstring."""

    def __init__(self, race=None):
        super().__init__(race if race else Races.HALF_ELF)

        self.age = Age(180, 20)
        self.size = Sizes.MEDIUM
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
        super().__init__(race if race else Races.HALF_ORC)
        self.ability_score_increases = [
            (Abilities.STRENGTH, 2),
            (Abilities.CONSTITUTION, 1)
        ]
        self.age = Age(75, 14)
        self.size = Sizes.MEDIUM
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
        super().__init__(race if race else Races.HALFLING)
        self.ability_score_increases = [
            (Abilities.DEXTERITY, 2)
        ]
        self.age = Age(150, 20)
        self.size = Sizes.SMALL
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


class Human(CharacterRace):
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
        self.age = Age(80, 20)
        self.size = Sizes.MEDIUM
        self.speed = 30
        self.languages = [
            Languages.COMMON,
            Strings.RANDOM
        ]
        # self._parse_random_abilities()


class VariantHuman(Human):
    """Class docstring."""

    def __init__(self, race=None):
        super().__init__(race if race else Races.HUMAN)
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
        super().__init__(race if race else Races.TIEFLING)
        self.ability_score_increases = [
            (Abilities.INTELLIGENCE, 1),
            (Abilities.CHARISMA, 2)
        ]
        self.age = Age(90, 20)
        self.size = Sizes.MEDIUM
        self.speed = 30
        self.languages = [
            Languages.COMMON,
            Languages.INFERNAL
        ]
        self.senses = [
            Darkvision(60)
        ]
