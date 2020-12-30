"""from controllers.category import Category
from controllers.product import Product

def create_categories() -> list:
    categories = []
    categories.append(Category("CAT-01","Eletronicos", "main", "MKT-01"))
    categories.append(Category("CAT-02","Moveis", "main", "MKT-"))
    categories.append(Category("CAT-03","Eletrodomesticos", "main"))
    return categories

def create_products() -> list:
    products = []
    products.append(Product("Celular", 7, 980.00, "redmi", 9.0, 7.0, 6.0, 3.0))
    products[0].set_category("CAT-01")
    products.append(Product("Base", 9, 50.00, "base em pó", 2.0, 1.0, 2.0, 2.0))
    products[1].set_category("CAT-02")
    products.append(Product("Pote de vidro", 3, 18.5, "pote vácuo", 5.0, 6.0, 3.0, 2.0))
    products[2].set_category("CAT-01")
    return products"""

from arq import read_marketplaces, read_categories, read_products
from textwrap import dedent

marketplaces = read_marketplaces()
categories = read_categories()
products = read_products()

option = 0
while option != 5:
    print(dedent(
        '''
        ############# MENU #############
        1 - Listar marketplaces
        2 - Listar categorias
        3 - Listar produtos
        '''
    ))
    option = int(input('Digite a opção: '))


def listing_marketplaces():
    print("############# MARKETPLACES #############")
    for key, market in marketplaces:
        print(key, ' - ', market)

def listing_categories():
    print("############# CATEGORIAS #############")
    for category in categories:
        print(category[1])

def listing_products():
    print("\n############# PRODUTOS #############")
    for product in products:
        print(product[0])