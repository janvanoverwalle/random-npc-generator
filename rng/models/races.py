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

    _name_to_race_map = None

    @classmethod
    def get(cls, race_name):
        """Method docstring."""
        if not cls._name_to_race_map:
            cls._name_to_race_map = {
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

        if not isinstance(race_name, (list, tuple)):
            race_name = [race_name]

        races = []
        for name in race_name:
            if not name or Strings.equals_ignore_case(name, Strings.RANDOM):
                races += [v for k, v in cls._name_to_race_map.items() if v not in races]
            else:
                name = cls._name_to_race_map.get(Races.to(name))
                if name not in races:
                    races.append(name)
        return races


    @classmethod
    def roll(cls, race_name=None, amount=1):
        """Method docstring."""

        if not amount:
            return None

        available_races = cls.get(race_name)

        results = [random.choice(c)() if isinstance(c, list) else c() for c in random.choices(available_races, k=amount)]
        return results[0] if amount == 1 else results

    @classmethod
    def roll_random(cls, amount=1):
        """Method docstring."""
        return cls.roll(Strings.RANDOM, amount)


class CharacterRace(object):
    """Class docstring."""

    def __init__(self, race_name):
        self._basic_rules = True

        self._name = race_name
        self._size = Sizes.NONE
        self._speed = 0
        self._age = None
        self._ability_score_increases = []
        self._original_ability_score_increases = None
        self._languages = []
        self._original_languages = None
        self._senses = []
        self._skills = []
        self._original_skills = None
        self._feats = []
        self._original_feats = None

    def __str__(self):
        return f'{self._name}'

    def _parse_random_ability_score_increases(self):
        if not self._ability_score_increases:
            return

        if self._original_ability_score_increases is None:
            self._original_ability_score_increases = self._ability_score_increases[:]
        else:
            self._ability_score_increases = self._original_ability_score_increases[:]

        abilities = Abilities.as_list()
        for ability in self._ability_score_increases:
            if ability[0] not in abilities:
                continue
            abilities.remove(ability[0])

        for index, ability in enumerate(self._ability_score_increases):
            if ability[0] != Strings.RANDOM:
                continue
            random_ability = abilities.pop(random.randint(1, len(abilities)-1))
            self._ability_score_increases[index] = (random_ability, ability[1])

    def _parse_random_languages(self):
        if not self._languages:
            return

        if self._original_languages is None:
            self._original_languages = self._languages[:]
        else:
            self._languages = self._original_languages[:]

        standard_languages = [l for l in Languages.standard_as_list() if l not in self._languages]
        exotic_languages = [l for l in Languages.exotic_as_list() if l not in self._languages]

        for index, language in enumerate(self._languages):
            if language != Strings.RANDOM:
                continue
            exotic_chance = random.randint(1, 100)
            language_list = exotic_languages if exotic_chance <= 10 else standard_languages
            random_language = language_list.pop(random.randint(1, len(language_list)-1))
            self._languages[index] = random_language

    def _parse_random_skills(self):
        if not self._skills:
            return

        if self._original_skills is None:
            self._original_skills = self._skills[:]
        else:
            self._skills = self._original_skills[:]

        skills = Skills.as_list()
        for skill in self._skills:
            if skill not in skills:
                continue
            skills.remove(skill)

        for index, skill in enumerate(self._skills):
            if skill != Strings.RANDOM:
                continue

            random_skill = skills.pop(random.randint(1, len(skills)-1))
            self._skills[index] = random_skill

    def _parse_random_feats(self):
        if not self._feats:
            return

        if self._original_feats is None:
            self._original_feats = self._feats[:]
        else:
            self._feats = self._original_feats[:]

        # TODO: Implement

    def _parse_random_abilities(self):
        self._parse_random_ability_score_increases()
        self._parse_random_languages()
        self._parse_random_skills()

    @property
    def name(self):
        """Method docstring."""
        return self._name

    @property
    def size(self):
        """Method docstring."""
        return self._size

    @property
    def speed(self):
        """Method docstring."""
        return self._speed

    @property
    def age(self):
        """Method docstring."""
        return self._age

    @property
    def ability_score_increases(self):
        """Method docstring."""
        return self._ability_score_increases

    @property
    def languages(self):
        """Method docstring."""
        return self._languages

    @property
    def senses(self):
        """Method docstring."""
        return self._senses

    @property
    def feats(self):
        """Method docstring."""
        return self._feats

    @property
    def skills(self):
        """Method docstring."""
        return self._skills

    def info_string(self):
        """Method docstring."""
        string = f'Race: {self._name}{Strings.LF}'
        string += f'  Sizes: {self._size}{Strings.LF}'
        string += f'  Speed: {self._speed} ft.{Strings.LF}'
        string += f'  Age: {self._age}{Strings.LF}'
        if self._ability_score_increases:
            string += f'  Ability Score Increases:{Strings.LF}'
            for elem in self._ability_score_increases:
                string += f'    {elem[0]}: {elem[1]}{Strings.LF}'
        if self._senses:
            string += f'  Senses:{Strings.LF}'
            for elem in self._senses:
                string += f'    {elem}{Strings.LF}'
        if self._languages:
            string += f'  Languages:{Strings.LF}'
            for elem in self._languages:
                string += f'    {elem}{Strings.LF}'
        if self._skills:
            string += f'  Skills:{Strings.LF}'
            for elem in self._skills:
                string += f'    {elem}{Strings.LF}'
        return string.strip()

    def roll_random_ability_score_increases(self):
        """Method docstring."""
        self._parse_random_ability_score_increases()

    def roll_random_languages(self):
        """Method docstring."""
        self._parse_random_languages()

    def roll_random_skills(self):
        """Method docstring."""
        self._parse_random_skills()

    def roll_random_feats(self):
        """Method docstring."""
        self._parse_random_feats()

    def roll_random_abilities(self):
        """Method docstring."""
        self.roll_random_ability_score_increases()
        self.roll_random_languages()
        self.roll_random_skills()

    def roll_age(self, char_class=None):
        """Method docstring."""
        return self._age.roll_random(self, char_class)


class Dragonborn(CharacterRace):
    """Class docstring."""

    def __init__(self):
        super().__init__(Races.DRAGONBORN)
        self._ability_score_increases = [
            (Abilities.STRENGTH, 2),
            (Abilities.CHARISMA, 1)
        ]
        self._age = Age(80, 3, 15)
        self._size = Sizes.MEDIUM
        self._speed = 30
        self._languages = [
            Languages.COMMON,
            Languages.DRACONIC
        ]


class Dwarf(CharacterRace):
    """Class docstring."""

    def __init__(self, race_name=None):
        super().__init__(race_name if race_name else Races.DWARF)
        self._ability_score_increases = [
            (Abilities.CONSTITUTION, 2)
        ]
        self._age = Age(350, 20, 50)
        self._size = Sizes.MEDIUM
        self._speed = 25
        self._languages = [
            Languages.COMMON,
            Languages.DWARVISH
        ]
        self._senses = [
            Darkvision(60)
        ]


class HillDwarf(Dwarf):
    """Class docstring."""

    def __init__(self):
        super().__init__(Races.HILL_DWARF)
        self._ability_score_increases.append((Abilities.WISDOM, 1))


class MountainDwarf(Dwarf):
    """Class docstring."""

    def __init__(self):
        super().__init__(Races.MOUNTAIN_DWARF)
        self._ability_score_increases.append((Abilities.STRENGTH, 2))


class Elf(CharacterRace):
    """Class docstring."""

    def __init__(self, race_name=None):
        super().__init__(race_name if race_name else Races.ELF)
        self._ability_score_increases = [
            (Abilities.DEXTERITY, 2)
        ]
        self._age = Age(750, 20, 100)
        self._size = Sizes.MEDIUM
        self._speed = 30
        self._languages = [
            Languages.COMMON,
            Languages.ELVISH
        ]
        self._senses = [
            Darkvision(60)
        ]
        self._skills = [
            Skills.PERCEPTION
        ]


class HighElf(Elf):
    """Class docstring."""

    def __init__(self):
        super().__init__(Races.HIGH_ELF)
        self._ability_score_increases.append((Abilities.INTELLIGENCE, 1))


class WoodElf(Elf):
    """Class docstring."""

    def __init__(self):
        super().__init__(Races.WOOD_ELF)
        self._ability_score_increases.append((Abilities.WISDOM, 1))
        self._speed = 35


class DarkElf(Elf):
    """Class docstring."""

    def __init__(self):
        super().__init__(Races.DARK_ELF)
        self._basic_rules = False

        self._ability_score_increases.append((Abilities.CHARISMA, 1))
        self._senses = [
            Darkvision(120)
        ]


class Gnome(CharacterRace):
    """Class docstring."""

    def __init__(self, race_name=None):
        super().__init__(race_name if race_name else Races.GNOME)
        self._ability_score_increases = [
            (Abilities.INTELLIGENCE, 2)
        ]
        self._age = Age((350, 500), 40)
        self._size = Sizes.SMALL
        self._speed = 25
        self._languages = [
            Languages.COMMON,
            Languages.GNOMISH
        ]
        self._senses = [
            Darkvision(60)
        ]


class RockGnome(Gnome):
    """Class docstring."""

    def __init__(self):
        super().__init__(Races.ROCK_GNOME)
        self._ability_score_increases.append((Abilities.CONSTITUTION, 1))


class ForestGnome(Gnome):
    """Class docstring."""

    def __init__(self):
        super().__init__(Races.FOREST_GNOME)
        self._basic_rules = False

        self._ability_score_increases.append((Abilities.DEXTERITY, 1))


class HalfElf(CharacterRace):
    """Class docstring."""

    def __init__(self, race_name=None):
        super().__init__(race_name if race_name else Races.HALF_ELF)

        self._age = Age(180, 20)
        self._size = Sizes.MEDIUM
        self._speed = 30
        self._ability_score_increases = [
            (Abilities.CHARISMA, 2),
            (Strings.RANDOM, 1),
            (Strings.RANDOM, 1)
        ]
        self._languages = [
            Languages.COMMON,
            Languages.ELVISH,
            Strings.RANDOM
        ]
        self._senses = [
            Darkvision(60)
        ]
        self._skills = [
            Strings.RANDOM,
            Strings.RANDOM
        ]
        # self._parse_random_abilities()


class HalfOrc(CharacterRace):
    """Class docstring."""

    def __init__(self, race_name=None):
        super().__init__(race_name if race_name else Races.HALF_ORC)
        self._ability_score_increases = [
            (Abilities.STRENGTH, 2),
            (Abilities.CONSTITUTION, 1)
        ]
        self._age = Age(75, 14)
        self._size = Sizes.MEDIUM
        self._speed = 30
        self._languages = [
            Languages.COMMON,
            Languages.ORC
        ]
        self._senses = [
            Darkvision(60)
        ]
        self._skills = [
            Skills.INTIMIDATION
        ]


class Halfling(CharacterRace):
    """Class docstring."""

    def __init__(self, race_name=None):
        super().__init__(race_name if race_name else Races.HALFLING)
        self._ability_score_increases = [
            (Abilities.DEXTERITY, 2)
        ]
        self._age = Age(150, 20)
        self._size = Sizes.SMALL
        self._speed = 25
        self._languages = [
            Languages.COMMON,
            Languages.HALFLING
        ]


class LightfootHalfling(Halfling):
    """Class docstring."""

    def __init__(self):
        super().__init__(Races.LIGHTFOOT_HALFLING)
        self._ability_score_increases.append((Abilities.CHARISMA, 1))


class StoutHalfling(Halfling):
    """Class docstring."""

    def __init__(self):
        super().__init__(Races.STOUT_HALFLING)
        self._ability_score_increases.append((Abilities.CONSTITUTION, 1))


class Human(CharacterRace):
    """Class docstring."""

    def __init__(self, race_name=None):
        super().__init__(race_name if race_name else Races.HUMAN)
        self._ability_score_increases = [
            (Abilities.STRENGTH, 1),
            (Abilities.DEXTERITY, 1),
            (Abilities.CONSTITUTION, 1),
            (Abilities.INTELLIGENCE, 1),
            (Abilities.WISDOM, 1),
            (Abilities.CHARISMA, 1)
        ]
        self._age = Age(80, 20)
        self._size = Sizes.MEDIUM
        self._speed = 30
        self._languages = [
            Languages.COMMON,
            Strings.RANDOM
        ]
        # self._parse_random_abilities()


class VariantHuman(Human):
    """Class docstring."""

    def __init__(self, race_name=None):
        super().__init__(race_name if race_name else Races.HUMAN)
        self._ability_score_increases = [
            (Strings.RANDOM, 1),
            (Strings.RANDOM, 1)
        ]
        self._skills = [
            Strings.RANDOM
        ]
        self._feats = [
            Strings.RANDOM
        ]
        # self._parse_random_abilities()


class Tiefling(CharacterRace):
    """Class docstring."""

    def __init__(self, race_name=None):
        super().__init__(race_name if race_name else Races.TIEFLING)
        self._ability_score_increases = [
            (Abilities.INTELLIGENCE, 1),
            (Abilities.CHARISMA, 2)
        ]
        self._age = Age(90, 20)
        self._size = Sizes.MEDIUM
        self._speed = 30
        self._languages = [
            Languages.COMMON,
            Languages.INFERNAL
        ]
        self._senses = [
            Darkvision(60)
        ]
