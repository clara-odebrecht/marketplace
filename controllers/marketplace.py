class Marketplace:
    def __init__(self, identifier, description) -> None:
        self.__identifier = identifier
        self.__description = description

    def get_identifier(self) -> str:
        return self.__identifier
    def get_description(self) -> str:
        return self.__description

    def set_identifier(self, value) -> None:
        self.__identifier = value
    def set_description(self, value) -> None:
        self.__description = value

    def show_all(self) -> None:
        print("Identificação: ", self.__identifier)
        print("Descrição: ", self.__description)