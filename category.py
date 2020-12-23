class Category():
    def __init__(self, identifier, description, category_type, marketplace) -> None:
        self.__identifier = identifier
        self.__description = description
        self.__category_type = category_type
        self.__marketplace = marketplace
        self.__sub_category = []

    def get_identifier(self) -> str:
        return self.__identifier
    def get_description(self) -> str:
        return self.__description
    def get_category_type(self) -> str:
        return self.__category_type
    def get_marketplace(self) -> str:
        return self.__marketplace
    def get_sub_category(self) -> list:
        return self.__sub_category

    def set_identifier(self, value) -> None:
        self.__identifier = value
    def set_description(self, value) -> None:
        self.__description = value
    def set_category_type(self, value) -> None:
        self.__category_type = value
    def set_marketplace(self, value) -> None:
        self.__marketplace = value
    def set_sub_category(self, value) -> None:
        self.__sub_category.append(value)

    def show_all(self) -> None:
        print("Identificação: ", self.get_identifier())
        print("Descrição: ", self.get_description())
        if self.__category_type == "main":
            print("Tipo de categoria: Categoria Principal")
        else:
            print("Tipo de categoria: Sub Categoria")
        print("Marketplace: ", self.get_marketplace())
        if self.__sub_category == []:
            print("Sub Categorias: ## Não cadastrado ##")
        else:
            print("Sub Categorias: ")
            for sub_category in self.__sub_category:
                print(sub_category, " - ")
            
