"""
Module docstring.
"""
import json
from pathlib import Path
from rng.helpers.utils import Utils


class Professions(object):
    """Class docstring."""

    KEY = 'profession'

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

    _json_path = Path(__file__).parent.parent / 'json' / 'character_professions.json'
    _profession_data = {}
    _categories = []
    _professions = []

    @classmethod
    def _load_json_data(cls, force_update=False):
        if cls._profession_data and not force_update:
            return

        cls._profession_data.clear()

        with open(f'{cls._json_path}', encoding='utf8') as json_file:
            cls._profession_data = json.load(json_file)

    @classmethod
    def data(cls):
        """Method docstring."""
        cls._load_json_data()
        return cls._profession_data

    @classmethod
    def as_list(cls):
        """Method docstring."""
        return cls.professions()

    @classmethod
    def categories(cls):
        """Method docstring."""
        if cls._categories:
            return cls._categories

        cls._load_json_data()

        cat_dict = cls._profession_data.get(cls.CATEGORIES)

        if not cat_dict:
            return None

        cls._categories = [v for k, v in cat_dict.items()]

        return cls._categories

    @classmethod
    def professions(cls):
        """Method docstring."""
        if cls._professions:
            return cls._professions

        cls._load_json_data()

        prof_dict = cls._profession_data.get(cls.PROFESSIONS)

        if not prof_dict:
            return None

        cls._professions = Utils.scan_for_values_with_key(prof_dict, cls.PROFESSION)

        return cls._professions

    @classmethod
    def is_valid(cls, obj):
        """Method docstring."""
        try:
            return obj.strip().lower() in cls.as_list()
        except Exception:
            return False

    @classmethod
    def to_category(cls, obj):
        """Method docstring."""
        try:
            for c in cls.categories():
                if c.lower() == obj.lower():
                    return c
        except Exception:
            return obj

    @classmethod
    def to_profession(cls, obj):
        """Method docstring."""
        try:
            for p in cls.professions():
                if p.lower() == obj.lower():
                    return p
        except Exception:
            return obj
