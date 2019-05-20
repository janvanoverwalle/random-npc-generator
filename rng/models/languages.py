"""
Module docstring.
"""


class Languages(object):
    """Class docstring."""

    # Standard
    COMMON = 'common'
    DWARVISH = 'dwarvish'
    ELVISH = 'elvish'
    GIANT = 'giant'
    GNOMISH = 'gnomish'
    GOBLIN = 'goblin'
    HALFLING = 'halfling'
    ORC = 'orc'

    # Exotic
    ABYSSAL = 'abyssal'
    CELESTIAL = 'celestial'
    DRACONIC = 'draconic'
    DEEP_SPEECH = 'deep speech'
    INFERNAL = 'infernal'
    PRIMORDIAL = 'primordial'
    SYLVAN = 'sylvan'
    UNDERCOMMON = 'undercommon'
    DRUIDIC = 'druidic'

    @classmethod
    def as_list(cls, subset=None):
        """Method docstring."""
        subset = subset.strip().lower()
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
