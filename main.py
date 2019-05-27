"""
Module docstring.
"""
from rng.models.characters import Characters
from rng.models.names import CharacterNames
from rng.models.professions import CharacterProfessions
from rng.models.races import CharacterRaces
from rng.models.genders import CharacterGenders
from rng.models.descriptions import CharacterDescriptions
from rng.resources.data.strings import Strings
from rng.resources.data.races import Races


def roll_independently():
    """Function docstring."""

    # Gender
    rolled_gender = CharacterGenders.roll_random()

    # Race
    rolled_race = CharacterRaces.roll_random()
    # rolled_race = CharacterRaces.roll(CharacterRaces.DRAGONBORN)

    # Profession
    rolled_profession = CharacterProfessions.roll_random('city')

    # Name
    rolled_name = CharacterNames.roll_random(rolled_race, rolled_gender)

    print(f'{rolled_name}')
    print(f'{rolled_gender}')
    print(f'{rolled_race}')
    print(f'{rolled_profession}')


def roll_character():
    """Function docstring."""
    npc = Characters.roll_npc(**{'race': Races.HALF_ELF})

    print(f'{npc.detailed_description(full_details=False)}')


def main():
    """Function docstring."""
    # roll_independently()
    roll_character()


def create_description_data():
    """Function docstring."""
    import json
    from pathlib import Path
    from rng.helpers.definition_lookup import DefinitionLookup

    json_path = Path(__file__).parent / 'rng' / 'resources' / 'json' / 'descr.json'
    with open(f'{json_path}', encoding='utf8') as json_file:
        json_data = json.load(json_file)

    def create_entry(w, d):
        ret = {}
        ret['WORD'] = w
        if definition:
            ret['DEFINITION'] = d
        return ret

    data = {}
    already_looked_up = []
    count = 0
    for element in json_data:
        count += 1
        print(f'{element} ({count}/{len(json_data)})')
        meaning = DefinitionLookup.meaning_of(element)
        if not meaning:
            print(f'  No meaning found')
            continue
        for k, v in meaning.items():
            key = k.upper()
            if key not in data:
                data[key] = []
            if element in already_looked_up:
                print(f'  Already in set, skipping')
                continue
            definition = v[0].get(DefinitionLookup.DEFINITION)
            if not definition:
                print(f'  No definition found')
            data[key].append(create_entry(element, definition))
            already_looked_up.append(element)
            break

    output_json_path = Path(__file__).parent / 'rng' / 'resources' / 'json' / 'descr_output.json'
    with open(f'{output_json_path}', 'w') as json_file:
        json.dump(data, json_file, indent=4)

    with open(f'{json_path}', 'w') as json_file:
        json.dump(already_looked_up, json_file, indent=4)


if __name__ == '__main__':
    print(CharacterDescriptions.test() + Strings.LF)
    # main()
    # create_description_data()
