class Product():
    def __init__(self, name, price, quantity, description, weight, height, width, depth) -> None:
        self.__name = name
        self.__price = price
        self.__quantity = quantity
        self.__description = description
        self.__weight = weight
        self.__height = height
        self.__width = width
        self.__depth = depth
        self.__category = []
        self.__sub_category = []

    def get_name(self) -> str:
        return self.__name
    def get_price(self) -> str:
        return self.__price
    def get_quantity(self) -> str:
        return self.__quantity
    def get_description(self) -> str:
        return self.__description
    def get_category(self) -> str:
        return self.__category
    def get_sub_category(self) -> str:
        return self.__sub_category
    def get_weight(self) -> float:
        return self.__weight
    def get_height(self) -> float:
        return self.__height
    def get_width(self) -> float:
        return self.__width
    def get_depth(self) -> float:
        return self.__depth

    def set_name(self, value) -> None:
        self.__name = value
    def set_price(self, value) -> None:
        self.__price = value
    def set_quantity(self, value) -> None:
        self.__quantity = value
    def set_description(self, value) -> None:
        self.__description = value
    def set_category(self, value) -> None:
        self.__category = value
    def set_sub_category(self, value) -> None:
        self.__sub_category = value
    def set_weight(self, value) -> None:
        self.__weight = value
    def set_height(self, value) -> None:
        self.__height = value
    def set_width(self, value) -> None:
        self.__width = value
    def set_depth(self, value) -> None:
        self.__depth = value

    def verify_is_none(self, value, type_category):
        if value == [] or value == "":
            print(type_category, ": ## Não cadastrado ##")
        else:
            print(type_category, ": ", value)

    def show_all(self) -> None:
        print("Nome: ", self.__name)
        print("Preço: ", self.__price)
        print("Quantidade: ", self.__quantity)
        print("Descrição: ", self.__description)
        print("Peso: ", self.__weight, "kg")
        print("Altura: ", self.__height, "m")
        print("Largura: ", self.__width, "m")
        print("Profundidade: ", self.__depth, "m")
        self.verify_is_none(self.__category, "Categoria Principal")
        self.verify_is_none(self.__sub_category, "Sub Categoria")