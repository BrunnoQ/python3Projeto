from endereco import Endereco
from datetime import date, timedelta


class Cliente:
    def __init__(self, nome, data_nascimento, endereco):
        self.__nome = nome
        self.__data_nascimento = data_nascimento
        self.__endereco = endereco

    @property
    def nome(self):
        return self.__nome

    @property
    def data_nascimento(self) -> date:
        return self.__data_nascimento

    @property
    def endereco(self) -> Endereco:
        return self.__endereco

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @data_nascimento.setter
    def data_nascimento(self, data_nascimento):
        self.__data_nascimento = data_nascimento

    @endereco.setter
    def endereco(self, endereco):
        self.__endereco = endereco

    def obter_idade(self):
        return date.today().year - self.data_nascimento.year - ((date.today().month, date.today().day) <
                                                                (self.data_nascimento.month, self.data_nascimento.day))

    def __str__(self):
        return f'{self.__nome}, {self.__data_nascimento}, {self.__endereco}'
