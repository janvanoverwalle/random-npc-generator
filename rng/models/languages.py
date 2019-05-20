"""
Module docstring.
"""


class Languages(object):
    """Class docstring."""

    # Standard
    COMMON = 'Common'
    DWARVISH = 'Dwarvish'
    ELVISH = 'Elvish'
    GIANT = 'Giant'
    GNOMISH = 'Gnomish'
    GOBLIN = 'Goblin'
    HALFLING = 'Halfling'
    ORC = 'Orc'

    # Exotic
    ABYSSAL = 'Abyssal'
    CELESTIAL = 'Celestial'
    DRACONIC = 'Draconic'
    DEEP_SPEECH = 'Deep Speech'
    INFERNAL = 'Infernal'
    PRIMORDIAL = 'Primordial'
    SYLVAN = 'Sylvan'
    UNDERCOMMON = 'Undercommon'
    DRUIDIC = 'Druidic'

    @classmethod
    def as_list(cls, subset=None):
        """Method docstring."""
        subset = subset.strip().lower() if subset else subset
        ret = []
        if not subset or subset == 'standard':
            ret += [
                cls.COMMON,
                cls.DWARVISH,
                cls.ELVISH,
                cls.GIANT,
                cls.GNOMISH,
                cls.GOBLIN,
                cls.HALFLING,
                cls.ORC
            ]
        if not subset or subset == 'exotic':
            ret += [
                cls.ABYSSAL,
                cls.CELESTIAL,
                cls.DRACONIC,
                cls.DEEP_SPEECH,
                cls.INFERNAL,
                cls.PRIMORDIAL,
                cls.SYLVAN,
                cls.UNDERCOMMON,
                cls.DRUIDIC
            ]
        return ret

    @classmethod
    def standard_as_list(cls):
        """Method docstring."""
        return cls.as_list(subset='standard')

    @classmethod
    def exotic_as_list(cls):
        """Method docstring."""
        return cls.as_list(subset='exotic')

    @classmethod
    def iterate(cls, subset=None):
        """Method docstring."""
        for language in cls.as_list(subset):
            yield language
