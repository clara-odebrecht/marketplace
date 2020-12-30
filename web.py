from flask import Flask, render_template, request
from controllers.marketplace import Marketplace
from controllers.category import Category
from controllers.product import Product
from arq import create_marketplace, read_marketplaces, create_category, read_categories, create_product, read_products

app = Flask(__name__)

@app.route("/create-marketplace")
def create_marketplaces():
    return render_template('create_marketplace.html', title = "Cadastro Marketplace")

@app.route("/marketplaces", methods=["GET", "POST"])
def list_marketplaces():
    if request.method == "POST":
        create_marketplace(request.form)
    marketplaces = read_marketplaces()
    return render_template('listing_marketplaces.html', title = "Marketplaces", list = marketplaces)


@app.route("/create-category/<marketplace>")
def create_categories(marketplace):
    return render_template('create_category.html', title = "Cadastro Categoria", markeplace_identifier = marketplace)

@app.route("/marketplace-categories/<identifier>", methods=["GET", "POST"])
def list_categories(identifier):
    print(request.method)
    print(request.form)
    if request.method == "POST":
        create_category(request.form)
    categories = read_categories()
    return render_template('listing_categories.html', title = "Categorias", list = categories, markeplace_identifier = identifier)


@app.route("/create-product/<category>")
def create_products(category):
    return render_template('create_product.html', title = "Cadastro Produto", category_identifier = category)

@app.route("/marketplace-categories/category-products/<identifier>", methods=["GET", "POST"])
def list_products(identifier):
    if request.method == "POST":
        create_product(request.form)
    products = read_products()
    return render_template('listing_products.html', title = "Produtos", list = products, category_identifier = identifier)

@app.route("/marketplace-categories/category-products/product/<identifier>")
def product_details(identifier):
    products = read_products()
    return render_template('product.html', list = products, product_name = identifier)

app.run(debug=True)