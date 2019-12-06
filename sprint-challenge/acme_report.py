import acme
from random import randint, uniform

adjectives = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
nouns = ['Anvil', 'Catapult' 'Disguise' 'Mousetrap', '???']


def generate_products(n_prods=30):
    """ does what it says on the tin. Generates products with randomized values and
    returns a list of them

        n_prods (optional) -
            number of products to generate - default 30
    """
    products = []

    for _ in range(n_prods):
        name = adjectives[randint(0, len(adjectives) - 1)
                          ] + ' ' + nouns[randint(0, len(nouns) - 1)]
        products.append(acme.Product(
                                name, _price=randint(5, 100),
                                _weight=randint(5, 100),
                                _flammability=uniform(0, 2.5)
                                )
                        )

    return products


def mean(ls):
    """ returns the mean of a list
    """
    return sum(ls) / len(ls)


def nunique(ls):
    """ returns the number of unique values of a list.
    """
    unique = []
    for val in ls:
        if val not in unique:
            unique.append(val)
    return len(unique)


def inventory_report(product_list):
    """ prints various statistics of a mock list of products that are generated.
    """

    names = [prod.name for prod in product_list]
    prices = [prod.price for prod in product_list]
    weights = [prod.weight for prod in product_list]
    flammabilities = [prod.flammability for prod in product_list]

    print('ACME CORPORATION OFFICIAL INVENTORY REPORT')
    print(f'Number of unique names: {nunique(names)}')
    print(f'Average price: {mean(prices)}')
    print(f'Average weight: {mean(weights)}')
    print(f'Average flammability: {mean(flammabilities)}')


if __name__ == '__main__':
    inventory_report(generate_products())
