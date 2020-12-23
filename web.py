from flask import Flask, render_template
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
    products[0].set_category("CAT-01")
    products.append(Product("Base", 9, 50.00, "base em pó", 2.0, 1.0, 2.0, 2.0))
    products[1].set_category("CAT-02")
    products.append(Product("Pote de vidro", 3, 18.5, "pote vácuo", 5.0, 6.0, 3.0, 2.0))
    products[2].set_category("CAT-01")
    return products

categories = create_categories()
products = create_products()

@app.route("/categories")
def list_categories():
    #title = "<h1>Categorias</h1><br/> "
    #index = "<ol> "
    #for category in categories:
    #    identifier = category.get_identifier()
    #    index = str(index) + f"<li><a href='category-products/{identifier}'>{category.get_description()}</a></li> "
    #index = str(index) + "</ol> "
    #return f'''{title} {index}'''
    return render_template('listing_categories.html', title = "Categorias", list = categories)


@app.route("/category-products/<identifier>")
def list_products(identifier):
    #title = "<h1>Produtos</h1><br/> "
    #index = "<ol> "
    #for product in products:
    #    if product.get_category() == str(identifier):
    #        index = str(index) + f"<li>{product.get_name()}</li> "
    #index = str(index) + "</ol> "
    #return f'''{title} {index}'''
    return render_template('listing_products.html', title = "Produtos", list = products, category_identifier = identifier)

@app.route("/category-products/product/<identifier>")
def product_details(identifier):
    return render_template('product.html', title = "Produto", list = products, product_name = identifier)

"""@app.route("/")
def teste():
    titulo = 'marketplace'
    return render_template('index.html', title = titulo)
"""
app.run()