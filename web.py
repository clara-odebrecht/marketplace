from flask import Flask, render_template
from marketplace import Marketplace
from category import Category
from product import Product

app = Flask(__name__)

def create_marketplaces() -> list:
    marketplaces = []
    marketplaces.append(Marketplace("MKT-01","Magazine Luiza"))
    marketplaces.append(Marketplace("MKT-02","Americanas"))
    marketplaces.append(Marketplace("MKT-03","Submarino"))
    return marketplaces

def create_categories() -> list:
    categories = []
    categories.append(Category("CAT-01","Eletronicos", "main", "MKT-01"))
    categories.append(Category("CAT-02","Moveis", "main", "MKT-01"))
    categories.append(Category("CAT-03","Eletrodomesticos", "main", "MKT-03"))
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

marketplaces = create_marketplaces()
categories = create_categories()
products = create_products()

@app.route("/marketplaces")
def list_marketplaces():
    return render_template('listing_marketplaces.html', title = "Marketplaces", list = marketplaces)

@app.route("/marketplace-categories/<identifier>")
def list_categories(identifier):
    #title = "<h1>Categorias</h1><br/> "
    #index = "<ol> "
    #for category in categories:
    #    identifier = category.get_identifier()
    #    index = str(index) + f"<li><a href='category-products/{identifier}'>{category.get_description()}</a></li> "
    #index = str(index) + "</ol> "
    #return f'''{title} {index}'''
    return render_template('listing_categories.html', title = "Categorias", list = categories, markeplace_identifier = identifier)


@app.route("/marketplace-categories/category-products/<identifier>")
def list_products(identifier):
    #title = "<h1>Produtos</h1><br/> "
    #index = "<ol> "
    #for product in products:
    #    if product.get_category() == str(identifier):
    #        index = str(index) + f"<li>{product.get_name()}</li> "
    #index = str(index) + "</ol> "
    #return f'''{title} {index}'''
    return render_template('listing_products.html', title = "Produtos", list = products, category_identifier = identifier)

@app.route("/marketplace-categories/category-products/product/<identifier>")
def product_details(identifier):
    return render_template('product.html', title = "Produto", list = products, product_name = identifier)

app.run()