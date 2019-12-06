import unittest
import random


class Product:
    """ Something Acme sells and some of its attributes.
    """
    # I personally prefer being able to see class data members explicitly
    # stated at the beginning.

    name = None
    price = None
    weight = None
    flammability = None
    identifier = None

    def __init__(self, _name, _price=10, _weight=20, _flammability=0.5):
        self.name = _name
        self.price = _price
        self.weight = _weight
        self.flammability = _flammability
        self.identifier = random.randint(1000000, 10000000)

    def stealability(self):
        """ returns a classified string based on the product's price and weight
        """
        rate = self.price / self.weight
        return ('Not so stealable...' if rate < 0.5 else
                ('Kinda stealable.' if rate < 1 else 'Very stealable!')
                )

    def explode(self):
        """
        returns a classified string based on the product's
            flmmability and weight.

        seems explodey.
        """
        rate = self.flammability * self.weight
        return ('...fizzle.' if rate < 10 else
                ('...boom!' if rate < 50 else '...BABOOM!!')
                )


class BoxingGlove(Product):
    """ ...it's a glove... that you wear...
    """

    def __init__(self, _name, _price=10, _weight=10, _flammability=0.5):
        super().__init__(self, _name, _price, _weight, _flammability)

    def explode(self):
        """ doesn't explode much...
        """
        return '...it\'s a glove.'

    def punch(self):
        """ returns a classified string based on the glove's weight
        """
        return ('That tickles.' if self.weight < 5 else
                ('Hey that hurt!' if self.weight < 15 else 'OUCH!')
                )