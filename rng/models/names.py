"""
Module docstring.
"""
import json
import random
from pathlib import Path
from rng.models.races import CharacterRaces
from rng.models.sexes import CharacterSexes


class CharacterNames(object):
    """Class docstring."""

    SOURCE = 'SOURCE'
    NAMES = 'NAMES'

    _json_path = Path(__file__).parent.parent / 'resources' / 'json' / 'names.json'
    _names = {}

    @classmethod
    def _create_empty_json_template(cls):
        return  # Safeguard (remove when required)

        all_races = CharacterRaces.as_list()
        all_sexes = CharacterSexes.as_list()
        sd = {s.upper():[] for s in all_sexes}
        sd['LAST'] = []
        data = {e.upper().replace(' ', '_').replace('-', ''):sd for e in all_races}

        with open(f'{cls._json_path}', 'w', encoding='utf8') as json_file:
            json.dump(data, json_file, indent=4)

    @classmethod
    def _load_json_data(cls, force_update=False):
        if cls._names and not force_update:
            return

        cls._names.clear()

        with open(f'{cls._json_path}', encoding='utf8') as json_file:
            data = json.load(json_file)

        cls._parse_name_data(data)

    @classmethod
    def _parse_name_data(cls, data):
        pass

    @classmethod
    def roll_random(cls, race=None, sex=None, amount=1):
        """Method docstring."""

        if not amount:
            return None

        cls._load_json_data()

        race_name_key = race.name.upper().replace(' ', '_').replace('-', '')
        tmp_dict1 = cls._names.get(race_name_key)

        if not tmp_dict1:
            pass  # TODO:

        sex_name_key = sex.sex.upper()
        tmp_dict2 = tmp_dict1.get(sex_name_key)

        if not tmp_dict2:
            pass  # TODO:

        for name_dict in tmp_dict2:
            source = name_dict.get(cls.SOURCE)
            names = name_dict.get(cls.NAMES)

            if names:
                break

        results = [CharacterName(s) for s in random.choices(names, k=amount)]
        return results[0] if amount == 1 else results


class CharacterName(object):
    """Class docstring."""

    def __init__(self, first_name, last_name=None):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        string = (
            f'Name: {self.first_name}'
            f'{" " + self.last_name if self.last_name else ""}'
        )
        return string
