import acme
import acme_report

import unittest
from acme import Product
from acme_report import generate_products, nouns, adjectives
from random import randint, uniform


class AcmeProductTests(unittest.TestCase):
    """ making sure Acme products correctly generated """

    def test_default_product_price(self):
        """ test default product price being 10 """

        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_random_product_stealability(self):
        """ test random product stealability being correct """

        price = randint(5, 100)
        weight = randint(5, 100)
        prod = Product('Test Product', price, weight)
        rate = prod.price / prod.weight
        val = ('Not so stealable...' if rate < 0.5 else
               ('Kinda stealable.' if rate < 1 else 'Very stealable!')
               )
        self.assertEqual(prod.stealability(), val)

    def test_random_product_explode(self):
        """ test random product explodability being correct """

        price = randint(5, 100)
        weight = randint(5, 100)
        prod = Product('Test Product', price, weight)
        rate = prod.flammability * prod.weight
        val = ('...fizzle.' if rate < 10 else
               ('...boom!' if rate < 50 else '...BABOOM!!')
               )
        self.assertEqual(prod.explode(), val)


class AcmeReportTests(unittest.TestCase):
    """ making sure acme tests are functioning as intended """

    def test_default_num_products(self):
        """ is the default length actually 30? """

        self.assertEqual(len(acme_report.generate_products()), 30)

    def test_legal_names(self):
        """ are the names correctly generated? """

        possible_names = []
        for adjective in adjectives:
            for noun in nouns:
                possible_names.append(adjective + ' ' + noun)

        generated_products = acme_report.generate_products()

        all_names_possible = True

        for i, prod in enumerate(generated_products):
            if prod.name not in possible_names:
                all_names_possible = False
                break

        self.assertEqual(all_names_possible, True)


if __name__ == '__main__':
    unittest.main()
