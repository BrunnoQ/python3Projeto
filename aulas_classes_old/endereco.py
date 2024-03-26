class Endereco:
    def __init__(self, logradouro, cep, numero, cidade, unidade_federada):
        self.__logradouro = logradouro
        self.__numero = numero
        self.__cidade = cidade
        self.__cep = cep
        self.__unidade_federada = unidade_federada

    # GETTERS
    @property
    def logradourou(self):
        return self.__logradouro

    @property
    def numero(self):
        return self.__numero

    @property
    def cidade(self):
        return self.__cidade

    @property
    def cep(self):
        return self.__cep

    @property
    def unidade_federada(self):
        return self.__unidade_federada

    # SETTERS
    @logradourou.setter
    def logradourou(self,logradourou):
        self.__logradouro = logradourou

    @numero.setter
    def numero(self, numero):
        self.__numero = numero

    @cidade.setter
    def cidade(self, cidade):
        self.__cidade = cidade

    @cep.setter
    def cep(self, cep):
        self.__cep = cep

    @unidade_federada.setter
    def unidade_federada(self, unidade_federada):
        self.__unidade_federada = unidade_federada

    def __str__(self):
        return f'{self.__logradouro}, {self.__numero}, {self.__cidade}, {self.__cep}, {self.__unidade_federada}'
