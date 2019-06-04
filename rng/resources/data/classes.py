"""
Module docstring.
"""


class Classes(object):
    """Class docstring."""

    KEY = 'class'

    BARBARIAN = 'Barbarian'
    PATH_OF_THE_BERSERKER = 'Path of the Berserker'  # PHB p.49
    PATH_OF_THE_TOTEM_WARRIOR = 'Path of the Totem Warrior'  # PHB p.50
    PATH_OF_THE_ANCESTRAL_GUARDIAN = 'Path of the Ancestral Guardian'  # XGtE p.9
    PATH_OF_THE_STORM_HERALD = 'Path of the Storm Herald'  # XGtE p.10
    PATH_OF_THE_ZEALOT = 'Path of the Zealot'  # XGtE p.11
    BARBARIAN_SUBCLASSES = [
        PATH_OF_THE_BERSERKER,
        PATH_OF_THE_TOTEM_WARRIOR,
        PATH_OF_THE_ANCESTRAL_GUARDIAN,
        PATH_OF_THE_STORM_HERALD,
        PATH_OF_THE_ZEALOT
    ]

    BARD = 'Bard'
    COLLEGE_OF_LORE = 'College of Lore'  # PHB p.54
    COLLEGE_OF_VALOR = 'College of Valor'  # PHB p.55
    COLLEGE_OF_GLAMOUR = 'College of Glamour'  # XGtE p.14
    COLLEGE_OF_SWORDS = 'College of Swords'  # XGtE p.15
    COLLEGE_OF_WHISPERS = 'College of Whispers'  # XGtE p.16
    BARD_SUBCLASSES = [
        COLLEGE_OF_LORE,
        COLLEGE_OF_VALOR,
        COLLEGE_OF_GLAMOUR,
        COLLEGE_OF_SWORDS,
        COLLEGE_OF_WHISPERS
    ]

    CLERIC = 'Cleric'
    DEATH_DOMAIN = 'Death Domain'  # DMG p.96
    KNOWLEDGE_DOMAIN = 'Knowledge Domain'  # PHB p.59
    LIFE_DOMAIN = 'Life Domain'  # PHB p.60
    LIGHT_DOMAIN = 'Light Domain'  # PHB p.60
    NATURE_DOMAIN = 'Nature Domain'  # PHB p.61
    TEMPEST_DOMAIN = 'Tempest Domain'  # PHB p.62
    TRICKERY_DOMAIN = 'Trickery Domain'  # PHB p.62
    WAR_DOMAIN = 'War Domain'  # PHB p.63
    FORGE_DOMAIN = 'Forge Domain'  # XGtE p.18
    GRAVE_DOMAIN = 'Grave Domain'  # XGtE p.19
    CLERIC_SUBCLASSES = [
        DEATH_DOMAIN,
        KNOWLEDGE_DOMAIN,
        LIFE_DOMAIN,
        LIGHT_DOMAIN,
        NATURE_DOMAIN,
        TEMPEST_DOMAIN,
        TRICKERY_DOMAIN,
        WAR_DOMAIN,
        FORGE_DOMAIN,
        GRAVE_DOMAIN
    ]

    DRUID = 'Druid'
    CIRCLE_OF_THE_LAND = 'Circle of the Land'  # PHB p.68
    CIRCLE_OF_THE_MOON = 'Circle of the Moon'  # PHB p.69
    CIRCLE_OF_DREAMS = 'Circle of Dreams'  # XGtE p.22
    CIRCLE_OF_THE_SHEPHERD = 'Circle of the Shepherd'  # XGtE p.23
    DRUID_SUBCLASSES = [
        CIRCLE_OF_THE_LAND,
        CIRCLE_OF_THE_MOON,
        CIRCLE_OF_DREAMS,
        CIRCLE_OF_THE_SHEPHERD
    ]

    FIGHTER = 'Fighter'
    BATTLE_MASTER = 'Battle Master'  # PHB p.73
    CHAMPION = 'Champion'  # PHB p.72
    ELDRITCH_KNIGHT = 'Eldritch Knight'  # PHB p.74
    ARCANE_ARCHER = 'Arcane Archer'  # XGtE p.28
    CAVALIER = 'Cavalier'  # XGtE p.30
    SAMURAI = 'Samurai'  # XGtE p.31
    FIGHTER_SUBCLASSES = [
        BATTLE_MASTER,
        CHAMPION,
        ELDRITCH_KNIGHT,
        ARCANE_ARCHER,
        CAVALIER,
        SAMURAI
    ]

    MONK = 'Monk'
    WAY_OF_THE_OPEN_HAND = 'Way of the Open Hand'  # PHB p.79
    WAY_OF_THE_FOUR_ELEMENTS = 'Way of the Four Elements'  # PHB p.80
    WAY_OF_SHADOW = 'Way of Shadow'  # PHB p.80
    WAY_OF_THE_DRUNKEN_MASTER = 'Way of the Drunken Master'  # XGtE p.33
    WAY_OF_THE_KENSEI = 'Way of the Kensei'  # XGtE p.34
    MONK_SUBCLASSES = [
        WAY_OF_THE_OPEN_HAND,
        WAY_OF_THE_FOUR_ELEMENTS,
        WAY_OF_SHADOW,
        WAY_OF_THE_DRUNKEN_MASTER,
        WAY_OF_THE_KENSEI
    ]

    PALADIN = 'Paladin'
    OATHBREAKER = 'Oathbreaker'  # DMG p.97
    OATH_OF_THE_ANCIENTS = 'Oath of the Ancients'  # PHB p.86
    OATH_OF_DEVOTION = 'Oath of Devotion'  # PHB p.85
    OATH_OF_VENGEANCE = 'Oath of Vengeance'  # PHB p.87
    OATH_OF_CONQUEST = 'Oath of Conquest'  # XGtE p.37
    OATH_OF_REDEMPTION = 'Oath of Redemption'  # XGtE p.38
    PALADIN_SUBCLASSES = [
        OATHBREAKER,
        OATH_OF_THE_ANCIENTS,
        OATH_OF_DEVOTION,
        OATH_OF_VENGEANCE,
        OATH_OF_CONQUEST,
        OATH_OF_REDEMPTION
    ]

    RANGER = 'Ranger'
    BEAST_MASTER = 'Beast Master'  # PHB p.93
    HUNTER = 'Hunter'  # PHB p.93
    GLOOM_STALKER = 'Gloom Stalker'  # XGtE p.41
    HORIZON_WALKER = 'Horizon Walker'  # XGtE p.42
    MONSTER_SLAYER = 'Monster Slayer'  # XGtE p.43
    RANGER_SUBCLASSES = [
        BEAST_MASTER,
        HUNTER,
        GLOOM_STALKER,
        HORIZON_WALKER,
        MONSTER_SLAYER
    ]

    ROGUE = 'Rogue'
    ARCANE_TRICKSTER = 'Arcane Trickster'  # PHB p.97
    ASSASSIN = 'Assassin'  # PHB p.97
    THIEF = 'Thief'  # PHB p.97
    INQUISITIVE = 'Inquisitive'  # XGtE p.45
    SCOUT = 'Scout'  # XGtE p.47
    ROGUE_SUBCLASSES = [
        ARCANE_TRICKSTER,
        ASSASSIN,
        THIEF,
        INQUISITIVE,
        SCOUT
    ]

    SORCERER = 'Sorcerer'
    DRACONIC_BLOODLINE = 'Draconic Bloodline'  # PHB p.102
    WILD_MAGIC = 'Wild Magic'  # PHB p.103
    DIVINE_SOUL = 'Divine Soul'  # XGtE p.50
    SHADOW_MAGIC = 'Shadow Magic'  # XGtE p.50
    SORCERER_SUBCLASSES = [
        DRACONIC_BLOODLINE,
        WILD_MAGIC,
        DIVINE_SOUL,
        SHADOW_MAGIC
    ]

    WARLOCK = 'Warlock'
    THE_ARCHFEY = 'The Archfey'  # PHB p.108
    THE_FIEND = 'The Fiend'  # PHB p.109
    THE_GREAT_OLD_ONE = 'The Great Old One'  # PHB p.109
    THE_CELESTIAL = 'The Celestial'  # XGtE p.54
    THE_HEXBLADE = 'The Hexblade'  # XGtE p.55
    WARLOCK_SUBCLASSES = [
        THE_ARCHFEY,
        THE_FIEND,
        THE_GREAT_OLD_ONE,
        THE_CELESTIAL,
        THE_HEXBLADE
    ]

    WIZARD = 'Wizard'
    SCHOOL_OF_ABJURATION = 'School of Abjuration'  # PHB p.115
    SCHOOL_OF_CONJURATION = 'School of Conjuration'  # PHB p.116
    SCHOOL_OF_DIVINATION = 'School of Divination'  # PHB p.116
    SCHOOL_OF_ENCHANTMENT = 'School of Enchantment'  # PHB p.117
    SCHOOL_OF_EVOCATION = 'School of Evocation'  # PHB p.117
    SCHOOL_OF_ILLUSION = 'School of Illusion'  # PHB p.118
    SCHOOL_OF_NECROMANCY = 'School of Necromancy'  # PHB p.118
    SCHOOL_OF_TRANSMUTATION = 'School of Transmutation'  # PHB p.119
    WAR_MAGIC = 'War Magic'  # XGtE p.59
    WIZARD_SUBCLASSES = [
        SCHOOL_OF_ABJURATION,
        SCHOOL_OF_CONJURATION,
        SCHOOL_OF_DIVINATION,
        SCHOOL_OF_ENCHANTMENT,
        SCHOOL_OF_EVOCATION,
        SCHOOL_OF_ILLUSION,
        SCHOOL_OF_NECROMANCY,
        SCHOOL_OF_TRANSMUTATION,
        WAR_MAGIC
    ]

    @classmethod
    def as_list(cls, subclasses=None):
        """Method docstring."""
        return cls.classes_as_list(subclasses)

    @classmethod
    def classes_as_list(cls, subclasses=None):
        """Method docstring."""
        if subclasses:
            if not isinstance(subclasses, (list, tuple)):
                subclasses = [subclasses]
            subclasses = [str(a).strip().lower() for a in subclasses]

        ret = []
        if not subclasses or any([sc for sc in cls.BARBARIAN_SUBCLASSES if sc in subclasses]):
            ret.append(cls.BARBARIAN)
        if not subclasses or any([sc for sc in cls.BARD_SUBCLASSES if sc in subclasses]):
            ret.append(cls.BARD)
        if not subclasses or any([sc for sc in cls.CLERIC_SUBCLASSES if sc in subclasses]):
            ret.append(cls.CLERIC)
        if not subclasses or any([sc for sc in cls.DRUID_SUBCLASSES if sc in subclasses]):
            ret.append(cls.DRUID)
        if not subclasses or any([sc for sc in cls.FIGHTER_SUBCLASSES if sc in subclasses]):
            ret.append(cls.FIGHTER)
        if not subclasses or any([sc for sc in cls.MONK_SUBCLASSES if sc in subclasses]):
            ret.append(cls.MONK)
        if not subclasses or any([sc for sc in cls.PALADIN_SUBCLASSES if sc in subclasses]):
            ret.append(cls.PALADIN)
        if not subclasses or any([sc for sc in cls.RANGER_SUBCLASSES if sc in subclasses]):
            ret.append(cls.RANGER)
        if not subclasses or any([sc for sc in cls.ROGUE_SUBCLASSES if sc in subclasses]):
            ret.append(cls.ROGUE)
        if not subclasses or any([sc for sc in cls.SORCERER_SUBCLASSES if sc in subclasses]):
            ret.append(cls.SORCERER)
        if not subclasses or any([sc for sc in cls.WARLOCK_SUBCLASSES if sc in subclasses]):
            ret.append(cls.WARLOCK)
        if not subclasses or any([sc for sc in cls.WIZARD_SUBCLASSES if sc in subclasses]):
            ret.append(cls.WIZARD)
        return ret

    @classmethod
    def subclasses_as_list(cls, classes=None):
        """Method docstring."""
        if classes:
            if not isinstance(classes, (list, tuple)):
                classes = [classes]
            classes = [str(a).strip().lower() for a in classes]

        ret = []
        if not classes or cls.BARBARIAN in classes:
            ret += [
                cls.PATH_OF_THE_BERSERKER,
                cls.PATH_OF_THE_TOTEM_WARRIOR,
                cls.PATH_OF_THE_ANCESTRAL_GUARDIAN,
                cls.PATH_OF_THE_STORM_HERALD,
                cls.PATH_OF_THE_ZEALOT
            ]
        if not classes or cls.BARD in classes:
            ret += [
                cls.COLLEGE_OF_LORE,
                cls.COLLEGE_OF_VALOR,
                cls.COLLEGE_OF_GLAMOUR,
                cls.COLLEGE_OF_SWORDS,
                cls.COLLEGE_OF_WHISPERS
            ]
        if not classes or cls.CLERIC in classes:
            ret += [
                cls.DEATH_DOMAIN,
                cls.KNOWLEDGE_DOMAIN,
                cls.LIFE_DOMAIN,
                cls.LIGHT_DOMAIN,
                cls.NATURE_DOMAIN,
                cls.TEMPEST_DOMAIN,
                cls.TRICKERY_DOMAIN,
                cls.WAR_DOMAIN,
                cls.FORGE_DOMAIN,
                cls.GRAVE_DOMAIN
            ]
        if not classes or cls.DRUID in classes:
            ret += [
                cls.CIRCLE_OF_THE_LAND,
                cls.CIRCLE_OF_THE_MOON,
                cls.CIRCLE_OF_DREAMS,
                cls.CIRCLE_OF_THE_SHEPHERD
            ]
        if not classes or cls.FIGHTER in classes:
            ret += [
                cls.BATTLE_MASTER,
                cls.CHAMPION,
                cls.ELDRITCH_KNIGHT,
                cls.ARCANE_ARCHER,
                cls.CAVALIER,
                cls.SAMURAI
            ]
        if not classes or cls.MONK in classes:
            ret += [
                cls.WAY_OF_THE_OPEN_HAND,
                cls.WAY_OF_THE_FOUR_ELEMENTS,
                cls.WAY_OF_SHADOW,
                cls.WAY_OF_THE_DRUNKEN_MASTER,
                cls.WAY_OF_THE_KENSEI
            ]
        if not classes or cls.PALADIN in classes:
            ret += [
                cls.OATHBREAKER,
                cls.OATH_OF_THE_ANCIENTS,
                cls.OATH_OF_DEVOTION,
                cls.OATH_OF_VENGEANCE,
                cls.OATH_OF_CONQUEST,
                cls.OATH_OF_REDEMPTION
            ]
        if not classes or cls.RANGER in classes:
            ret += [
                cls.BEAST_MASTER,
                cls.HUNTER,
                cls.GLOOM_STALKER,
                cls.HORIZON_WALKER,
                cls.MONSTER_SLAYER
            ]
        if not classes or cls.ROGUE in classes:
            ret += [
                cls.ARCANE_TRICKSTER,
                cls.ASSASSIN,
                cls.THIEF,
                cls.INQUISITIVE,
                cls.SCOUT
            ]
        if not classes or cls.SORCERER in classes:
            ret += [
                cls.DRACONIC_BLOODLINE,
                cls.WILD_MAGIC,
                cls.DIVINE_SOUL,
                cls.SHADOW_MAGIC
            ]
        if not classes or cls.WARLOCK in classes:
            ret += [
                cls.THE_ARCHFEY,
                cls.THE_FIEND,
                cls.THE_GREAT_OLD_ONE,
                cls.THE_CELESTIAL,
                cls.THE_HEXBLADE
            ]
        if not classes or cls.WIZARD in classes:
            ret += [
                cls.SCHOOL_OF_ABJURATION,
                cls.SCHOOL_OF_CONJURATION,
                cls.SCHOOL_OF_DIVINATION,
                cls.SCHOOL_OF_ENCHANTMENT,
                cls.SCHOOL_OF_EVOCATION,
                cls.SCHOOL_OF_ILLUSION,
                cls.SCHOOL_OF_NECROMANCY,
                cls.SCHOOL_OF_TRANSMUTATION,
                cls.WAR_MAGIC
            ]
        return ret

    @classmethod
    def is_valid(cls, obj):
        """Method docstring."""
        try:
            return obj.strip().lower() in cls.as_list()
        except Exception:
            return False

    @classmethod
    def to(cls, obj):
        """Method docstring."""
        try:
            for c in cls.as_list():
                if c.lower() == obj.lower():
                    return c
        except Exception:
            return obj