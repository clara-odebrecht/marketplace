def read_marketplaces() -> list:
    arq = open('marketplaces.txt', 'r')
    marketplaces = []
    for line in arq:
        lines = line.split()
        for mkt in lines:
            comas = mkt.split(';')
            marketplaces.append(comas)
    arq.close()
    return marketplaces

def read_categories() -> list:
    arq = open('categories.txt', 'r')
    categories = []
    for line in arq:
        lines = line.split()
        for ctg in lines:
            comas = ctg.split(';')
            categories.append(comas)
    arq.close()
    return categories

def read_products() -> list:
    arq = open('products.txt', 'r')
    products = []
    for pdt in arq:
        comas = pdt.split(';')
        products.append(comas)
        products[-1][-1] = products[-1][-1].rstrip('\n')
    arq.close()
    print(products)
    return products