"""
Module docstring.
"""
import json
import random
from pathlib import Path
from rng.models.classes import CharacterClasses
from rng.resources.data.abilities import Abilities
from rng.resources.data.skills import Skills
from rng.resources.data.strings import Strings


class CharacterProfessions(object):
    """Class docstring."""

    CATEGORIES = 'CATEGORIES'
    PROFESSIONS = 'PROFESSIONS'
    PROFESSION = 'PROFESSION'
    DESCRIPTION = 'DESCRIPTION'
    CLASSES = 'CLASSES'
    SKILLS = 'SKILLS'
    SAVING_THROWS = 'SAVING_THROWS'
    LOCALES = 'LOCALES'
    LOCALE = 'LOCALE'
    WEIGHT = 'WEIGHT'

    _json_path = Path(__file__).parent.parent / 'resources' / 'json' / 'character_professions.json'
    _categories = {}

    professions = []

    @classmethod
    def _load_json_data(cls, force_update=False):
        if cls._categories and cls.professions and not force_update:
            return

        cls._categories.clear()
        cls.professions.clear()

        with open(f'{cls._json_path}', encoding='utf8') as json_file:
            data = json.load(json_file)

        cls._parse_profession_data(data)

    @classmethod
    def _parse_profession_data(cls, data):
        if not data:
            return

        for k, v in data.items():
            if k == cls.CATEGORIES:
                cls._categories = v
            elif k == cls.PROFESSIONS:
                cls._parse_category_data(v)

    @classmethod
    def _parse_category_data(cls, data):
        for k, v in data.items():
            category = cls._categories[k]
            locales = v.get(cls.LOCALES)
            professions = v.get(cls.PROFESSIONS)
            cls._parse_profession_list(category, professions, locales)

    @classmethod
    def _parse_profession_list(cls, category, data, locale_data=None):
        for p_data in data:
            profession = p_data.get(cls.PROFESSION)
            description = p_data.get(cls.DESCRIPTION)
            assoc_class = p_data.get(cls.CLASSES)
            skills = p_data.get(cls.SKILLS)
            saving_throws = p_data.get(cls.SAVING_THROWS)
            locale_data = p_data.get(cls.LOCALES, locale_data)

            if cls.professions is None:
                cls.professions = []

            kwargs = {}
            if assoc_class:
                kwargs[cls.CLASSES] = assoc_class
            if skills:
                kwargs[cls.SKILLS] = skills
            if saving_throws:
                kwargs[cls.SAVING_THROWS] = saving_throws
            if locale_data:
                kwargs[cls.LOCALES] = locale_data

            profession_obj = CharacterProfession(profession, description, category, **kwargs)
            cls.professions.append(profession_obj)

    @classmethod
    def categories(cls):
        """Method docstring."""
        return [v for k, v in cls._categories.items()]

    @classmethod
    def roll_random(cls, locale=None, amount=1):
        """Method docstring."""

        if not amount:
            return None

        cls._load_json_data()

        possible_professions = [p for p in cls.professions if p.get_weight(locale) > 0]
        weights = [p.get_weight(locale) for p in possible_professions]
        results = random.choices(possible_professions, weights, k=amount)
        return results[0] if amount == 1 else results


class CharacterProfession(object):
    """Class docstring."""
    def __init__(self, name, description=None, category=None, **kwargs):
        assoc_class = kwargs.get(CharacterProfessions.CLASSES)
        skills = kwargs.get(CharacterProfessions.SKILLS)
        saving_throws = kwargs.get(CharacterProfessions.SAVING_THROWS)
        locale_data = kwargs.get(CharacterProfessions.LOCALES)

        self._name = name
        self._description = description.capitalize() if isinstance(description, str) else description
        self._category = category
        self._assoc_class = CharacterClasses.get(assoc_class)
        tmp_skills = [skills] if isinstance(skills, str) or skills is None else skills
        self._skills = [Skills.convert(s) for s in tmp_skills if s]
        tmp_saving_throws = [saving_throws] if isinstance(saving_throws, str) or saving_throws is None else saving_throws
        self._saving_throws = [Abilities.convert(s) for s in tmp_saving_throws if s]
        self._locale_data = locale_data

    @property
    def name(self):
        """Method docstring."""
        return self._name

    @property
    def description(self):
        """Method docstring."""
        return self._description

    @property
    def category(self):
        """Method docstring."""
        return self._category

    @property
    def associated_class(self):
        """Method docstring."""
        return self._assoc_class

    @property
    def skills(self):
        """Method docstring."""
        return self._skills

    @property
    def saving_throws(self):
        """Method docstring."""
        return self._saving_throws

    def __str__(self):
        # cat_str = f'[{self.category}] ' if self.category else ''
        string = f'Profession: {self._name}{Strings.LF}'
        string += f'  Description: {self._description}{Strings.LF}' if self._description else ''
        if self._saving_throws:
            string += f'  Saving Throws:{Strings.LF}'
            for elem in self._saving_throws:
                string += f'    {elem}{Strings.LF}'
        if self._skills:
            string += f'  Skills:{Strings.LF}'
            for elem in self._skills:
                string += f'    {elem}{Strings.LF}'
        return string.strip()

    def __repr__(self):
        return f'{self._name}'

    def get_weight(self, locale=None):
        """Method docstring."""

        if not locale:
            return 1
        for data in self._locale_data:
            loc = data.get(CharacterProfessions.LOCALE)
            if not loc:
                continue
            if locale.lower() == loc.lower():
                try:
                    return float(data.get(CharacterProfessions.WEIGHT, 0))
                except (TypeError, ValueError):
                    continue
        return 1
