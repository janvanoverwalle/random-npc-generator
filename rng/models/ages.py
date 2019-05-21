"""
Module docstring.
"""


class Age(object):
    """Class docstring"""

    def __init__(self, lifespan, physical, mental, current=None):
        self.lifespan = lifespan  # Could be a tuple indicating a range
        self.physical_maturation = physical
        self.mental_maturation = mental
        self.current = current
        self.adulthood = max(self.physical_maturation, self.mental_maturation)

    def __str__(self):
        return f'Lifespan: {self.lifespan}, Adulthood: {self.adulthood}'
