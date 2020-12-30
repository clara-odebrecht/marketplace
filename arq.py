from datetime import datetime

def create_marketplace(marketplace) -> None:
    arq = open('marketplaces.txt', 'a')
    text = '\n' + marketplace.get('identifier') + ";" + marketplace.get('description')
    arq.write(text)
    create_log('create_marketplace')
    arq.close()

def read_marketplaces() -> list:
    arq = open('marketplaces.txt', 'r')
    marketplaces = []
    for line in arq:
        lines = line.split()
        for mkt in lines:
            comas = mkt.split(';')
            marketplaces.append(comas)
    arq.close()
    create_log('read_marketplaces')
    return marketplaces


def create_category(category) -> None:
    arq = open('categories.txt', 'a')
    text = '\n' + category.get('identifier') + ";" + category.get('description') + ";" + category.get("type") + ";" + category.get("marketplace")
    arq.write(text)
    create_log('create_category')
    arq.close()

def read_categories() -> list:
    arq = open('categories.txt', 'r')
    categories = []
    for line in arq:
        lines = line.split()
        for ctg in lines:
            comas = ctg.split(';')
            categories.append(comas)
    arq.close()
    create_log('categorias')
    return categories


def create_product(product) -> None:
    arq = open('products.txt', 'a')
    text = '\n' + product.get('name') + ";" + product.get('price') + ";" + product.get('quantity') + ";" + product.get('description') + ";" + product.get('width') + ";" + product.get('height') + ";" + product.get('depth') + ";" + product.get('weigth') + ";" + product.get('category')
    arq.write(text)
    create_log('create_product')
    arq.close()

def read_products() -> list:
    arq = open('products.txt', 'r')
    products = []
    for pdt in arq:
        comas = pdt.split(';')
        products.append(comas)
        products[-1][-1] = products[-1][-1].rstrip('\n')
    arq.close()
    create_log('produtos')
    return products

def create_log(value: str) -> None:
    arq = open('logs.txt', "a")
    info = str(datetime.now()) + ' Foi consultado ' + value + '\n'
    arq.write(info)
    arq.close()