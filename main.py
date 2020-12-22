from category import Category
from product import Product

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

print("############# CATEGORIAS #############")
for category in categories:
    category.show_all()

print("\n############# PRODUTOS #############")
for product in products:
    product.show_all()