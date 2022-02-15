from datetime import datetime
from random import randint

"""
Encapsulamento no PYTHON só existe POR convenção!
_ = protected NAO ACESSAR DIRETAMENTE
__ = privado NAO ACESSAR DIRETAMENTE de forma ALGUMA

"""
class Pessoa:
    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))  # atributo static

    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    # Getter por convenção o "_" vai na frente
    @property
    def nome(self):
        return self._nome

    # Setter
    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def idade(self):
        return self._idade

    # Setter
    @idade.setter
    def idade(self, idade):
        if isinstance(idade, str):
            print('wtf??')
        else:
            print(type(idade))
            self._idade = idade

    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome}, esta comendo')

        self.comendo = True
        print(f'{self.nome}, esta comendo {alimento}')

    def get_ano_nascimento(self):
        return self.ano_atual - self.idade

    # Metodo da classe, retorna um OBJETO desta classe CLS poderia ser qualquer nome, assim como SELF
    @classmethod
    def por_ano_nacimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)

    # Diferentemente de um class method esse camarada não precisa de nenhuma referencia 'CLS'
    @staticmethod
    def gera_id():
        rand = randint(10000, 19999)
        return rand

