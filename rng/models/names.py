"""
Module docstring.
"""
import json
import random
from pathlib import Path
from rng.models.races import CharacterRaces
from rng.models.genders import CharacterGenders


class CharacterNames(object):
    """Class docstring."""

    SOURCE = 'SOURCE'
    NAMES = 'NAMES'
    LAST = 'LAST'
    REF = 'ref:'

    _json_path = Path(__file__).parent.parent / 'resources' / 'json' / 'character_names.json'
    _name_data = {}

    @classmethod
    def _create_empty_json_template(cls):
        return  # Safeguard (remove when required)

        all_races = CharacterRaces.as_list()
        all_genders = CharacterGenders.as_list()
        gender_dict = {s.upper():[] for s in all_genders}
        gender_dict[cls.LAST] = []
        data = {e.upper().replace(' ', '_').replace('-', ''):gender_dict for e in all_races}

        with open(f'{cls._json_path}', 'w', encoding='utf8') as json_file:
            json.dump(data, json_file, indent=4)

    @classmethod
    def _load_json_data(cls, force_update=False):
        if cls._name_data and not force_update:
            return

        cls._name_data.clear()

        with open(f'{cls._json_path}', encoding='utf8') as json_file:
            cls._name_data = json.load(json_file)

    @classmethod
    def roll_random(cls, race=None, gender=None, amount=1, sources=None):
        """Method docstring."""

        if not amount:
            return None

        if sources:
            if isinstance(sources, str):
                sources = [sources]
            sources = [s.strip().upper().replace(' ', '_') for s in sources]

        cls._load_json_data()

        cls._selected_sources = sources

        if not race:
            race = CharacterRaces.roll_random()

        if not gender:
            gender = CharacterGenders.roll_random()

        first_names, last_names = cls._retrieve_names(race.name, gender.gender, sources)

        if not first_names:
            return None

        resulting_first_names = [s for s in random.choices(first_names, k=amount)]

        if not last_names:
            results = [CharacterName(s) for s in random.choices(resulting_first_names, k=amount)]
            return results[0] if amount == 1 else results

        resulting_last_names = [s for s in random.choices(last_names, k=amount)]

        results = []
        for index, first_name in enumerate(resulting_first_names):
            last_name = resulting_last_names[index]
            results.append(CharacterName(first_name, last_name))
        return results[0] if amount == 1 else results

    @classmethod
    def _retrieve_race_data(cls, race_key):
        race_key = race_key.upper().replace(' ', '_').replace('-', '')
        # print(f'{race_namrace_keye_key}')
        race_data_dict = cls._name_data.get(race_key)

        if not race_data_dict:
            error_msg = f'No correspondig name data found for given race "{race_key}"'
            raise NotImplementedError(error_msg)

        if isinstance(race_data_dict, str):
            # print(f'  Found a reference: {race_data_dict}')
            substr_index = race_data_dict.find(cls.REF) + len(cls.REF)
            race_data_dict = cls._name_data.get(race_data_dict[substr_index:])

        return race_data_dict

    @classmethod
    def _retrieve_names(cls, race_key, gender_key, sources=None):
        race_data = cls._retrieve_race_data(race_key)

        gender_key = gender_key.upper()
        # print(f'{gender_key}')
        gender_data = race_data.get(gender_key)

        if not gender_data:
            error_msg = f'No correspondig name data found for given gender "{gender_data}"'
            raise NotImplementedError(error_msg)

        first_names, references = cls._retrieve_first_names(gender_data, sources)        

        for ref in references:
            substr_index = ref.find(cls.REF) + len(cls.REF)
            ref_first, _ = cls._retrieve_names(ref[substr_index:], gender_key)
            first_names += ref_first

        last_names = []
        last_name_data_dict = race_data.get(cls.LAST)
        if last_name_data_dict:
            last_names, references = cls._retrieve_last_names(last_name_data_dict, sources)

            for ref in references:
                substr_index = ref.find(cls.REF) + len(cls.REF)
                _, ref_last = cls._retrieve_names(ref[substr_index:], gender_key)
                last_names += ref_last

        return first_names, last_names

    @classmethod
    def _retrieve_first_names(cls, gender_data, sources=None):
        first_names = []
        references = []

        for name_dict in gender_data:
            source = name_dict.get(cls.SOURCE)
            if sources and source not in sources:
                continue
            name_list = name_dict.get(cls.NAMES)
            if not name_list:
                continue
            references += [n for n in name_list if cls.REF in n and n not in references]
            name_list = [n for n in name_list if cls.REF not in n]
            first_names += name_list

        return first_names, references

    @classmethod
    def _retrieve_last_names(cls, data, sources=None):
        last_names = []
        references = []

        for name_dict in data:
            source = name_dict.get(cls.SOURCE)
            if sources and source not in sources:
                continue
            name_list = name_dict.get(cls.NAMES)
            if not name_list:
                continue
            references += [n for n in name_list if cls.REF in n and n not in references]
            name_list = [n for n in name_list if cls.REF not in n]
            last_names += name_list
        
        return last_names, references


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

    def __repr__(self):
        return str(self)
