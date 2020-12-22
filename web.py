from flask import Flask
from product import Product
from category import Category
#from main import create_products, create_categories

app = Flask(__name__)

def create_categories() -> list:
    categories = []
    categories.append(Category("CAT-01","Eletronicos", "main"))
    categories.append(Category("CAT-02","Moveis", "main"))
    categories.append(Category("CAT-03","Eletrodomesticos", "main"))
    return categories

def create_products() -> list:
    products = []
    products.append(Product("Celular", 7, 980.00, "redmi", 9.0, 7.0, 6.0, 3.0))
    products.append(Product("Base", 9, 50.00, "base em pó", 2.0, 1.0, 2.0, 2.0))
    products.append(Product("Pote de vidro", 3, 18.5, "pote vácuo", 5.0, 6.0, 3.0, 2.0))
    return products

categories = create_categories()
products = create_products()

@app.route("/categories")
def list_categories():
    title = "<h1>Categorias</h1><br/> "
    index = "<ol> "
    for category in categories:
        identifier = category.get_identifier()
        index = str(index) + f"<li><a href='category-products/{identifier}'>{category.get_description()}</a></li> "
    index = str(index) + "</ol> "
    return f'''{title} {index}'''


@app.route("/category-products/<identifier>")
def list_products(identifier):
    title = "<h1>Produtos</h1><br/> "
    index = "<ol> "
    for product in products:
        if product.get_category() == str(identifier):
            index = str(index) + f"<li>{product.get_name()}</li> "
    index = str(index) + "</ol> "
    return f'''{title} {index}'''

app.run()