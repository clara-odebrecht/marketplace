from flask import Flask, render_template
from controllers.marketplace import Marketplace
from controllers.category import Category
from controllers.product import Product
from arq import read_marketplaces, read_categories, read_products

app = Flask(__name__)

"""def create_marketplaces() -> list:
    marketplaces = []
    marketplaces.append(Marketplace("MKT-01","Magazine Luiza"))
    marketplaces.append(Marketplace("MKT-02","Americanas"))
    marketplaces.append(Marketplace("MKT-03","Submarino"))
    marketplaces.append(Marketplace("MKT-04","Shopee"))
    return marketplaces

def create_categories() -> list:
    categories = []
    categories.append(Category("CAT-01","Eletronicos", "main", "MKT-01"))
    categories.append(Category("CAT-02","Beleza", "main", "MKT-01"))
    categories.append(Category("CAT-03","Cozinha", "main", "MKT-02"))
    categories.append(Category("CAT-04","Eltrodomesticos", "main", "MKT-03"))
    categories.append(Category("CAT-05","Moveis", "main", "MKT-02"))
    return categories

def create_products() -> list:
    products = []
    products.append(Product("Celular", 7, 980.00, "redmi", 9.0, 7.0, 6.0, 3.0))
    products[0].set_category("CAT-01")
    products.append(Product("Base", 9, 50.00, "base em pó", 2.0, 1.0, 2.0, 2.0))
    products[1].set_category("CAT-02")
    products.append(Product("Pote de vidro", 3, 18.5, "pote vácuo", 5.0, 6.0, 3.0, 2.0))
    products[2].set_category("CAT-03")
    products.append(Product("Mouse", 3, 18.5, "longitech", 5.0, 6.0, 3.0, 2.0))
    products[3].set_category("CAT-01")
    products.append(Product("Teclado", 3, 18.5, "razer", 5.0, 6.0, 3.0, 2.0))
    products[4].set_category("CAT-01")
    products.append(Product("Air Fryer", 3, 18.5, "220", 5.0, 6.0, 3.0, 2.0))
    products[5].set_category("CAT-04")
    #products.append(Product("Tapete", 3, 18.5, "Persa", 5.0, 6.0, 3.0, 2.0))
    #products[6].set_category("CAT-05")
    return products

marketplaces = create_marketplaces()
categories = create_categories()
products = create_products()"""
marketplaces = read_marketplaces()
categories = read_categories()
products = read_products()

@app.route("/marketplaces")
def list_marketplaces():
    return render_template('listing_marketplaces.html', title = "Marketplaces", list = marketplaces)

@app.route("/marketplace-categories/<identifier>")
def list_categories(identifier):
    return render_template('listing_categories.html', title = "Categorias", list = categories, markeplace_identifier = identifier)

@app.route("/marketplace-categories/category-products/<identifier>")
def list_products(identifier):
    return render_template('listing_products.html', title = "Produtos", list = products, category_identifier = identifier)

@app.route("/marketplace-categories/category-products/product/<identifier>")
def product_details(identifier):
    return render_template('product.html', title = "Produto", list = products, product_name = identifier)

app.run(debug=True)