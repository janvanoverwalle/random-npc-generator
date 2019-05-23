"""
Module docstring.
"""
from rng.resources.data.abilities import Abilities


class Skills(object):
    """Class docstring."""

    # Strength
    ATHLETICS = 'Athletics'

    # Dexterity
    ACROBATICS = 'Acrobatics'
    SLEIGHT_OF_HAND = 'Sleight of Hand'
    STEALTH = 'Stealth'

    # Intelligence
    ARCANA = 'Arcana'
    HISTORY = 'History'
    INVESTIGATION = 'Investigation'
    NATURE = 'Nature'
    RELIGION = 'Religion'

    # Wisdom
    ANIMAL_HANDLING = 'Animal Handling'
    INSIGHT = 'Insight'
    MEDICINE = 'Medicine'
    PERCEPTION = 'Perception'
    SURVIVAL = 'Survival'

    # Charisma
    DECEPTION = 'Deception'
    INTIMIDATION = 'Intimidation'
    PERFORMANCE = 'Performance'
    PERSUASION = 'Persuasion'

    @classmethod
    def as_list(cls, abilities=None):
        """Method docstring."""
        if abilities:
            if not isinstance(abilities, (list, tuple)):
                abilities = [abilities]
            abilities = [str(a).strip().lower() for a in abilities]
        else:
            abilities = Abilities.as_list()
        ret = []
        if Abilities.STRENGTH in abilities:
            ret += [
                cls.ATHLETICS
            ]
        if Abilities.DEXTERITY in abilities:
            ret += [
                cls.ACROBATICS,
                cls.SLEIGHT_OF_HAND,
                cls.STEALTH
            ]
        if Abilities.INTELLIGENCE in abilities:
            ret += [
                cls.ARCANA,
                cls.HISTORY,
                cls.INVESTIGATION,
                cls.NATURE,
                cls.RELIGION
            ]
        if Abilities.WISDOM in abilities:
            ret += [
                cls.ANIMAL_HANDLING,
                cls.INSIGHT,
                cls.MEDICINE,
                cls.PERCEPTION,
                cls.SURVIVAL
            ]
        if Abilities.CHARISMA in abilities:
            ret += [
                cls.DECEPTION,
                cls.INTIMIDATION,
                cls.PERFORMANCE,
                cls.PERSUASION
            ]
        return ret

    @classmethod
    def iterate(cls, abilities=None):
        """Method docstring."""
        for skill in cls.as_list(abilities):
            yield skill

    @classmethod
    def convert(cls, obj):
        """Method docstring."""
        if obj is None:
            return None
        parsed_string = ''.join([c for c in str(obj).lower() if c.isalpha()])
        for skill in cls.iterate():
            parsed_skill = ''.join([c for c in skill.lower() if c.isalpha()])
            if parsed_string == parsed_skill:
                return skill
        return str(obj)
