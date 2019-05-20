"""
Module docstring.
"""
from rng.models.abilities import Abilities


class Skills(object):
    """Class docstring."""

    # Strength
    ATHLETICS = 'athletics'

    # Dexterity
    ACROBATICS = 'acrobatics'
    SLEIGHT_OF_HAND = 'sleight of hand'
    STEALTH = 'stealth'

    # Intelligence
    ARCANA = 'arcana'
    HISTORY = 'history'
    INVESTIGATION = 'investigation'
    NATURE = 'nature'
    RELIGION = 'religion'

    # Wisdom
    ANIMAL_HANDLING = 'animal handling'
    INSIGHT = 'insight'
    MEDICINE = 'medicine'
    PERCEPTION = 'perception'
    SURVIVAL = 'survival'

    # Charisma
    DECEPTION = 'deception'
    INTIMIDATION = 'intimidation'
    PERFORMANCE = 'performance'
    PERSUASION = 'persuasion'

    @classmethod
    def as_list(cls, abilities=None):
        """Method docstring."""
        if not isinstance(abilities, (list, tuple)):
            abilities = [abilities]
        abilities = [str(a).strip().lower() for a in abilities]
        if not abilities:
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
