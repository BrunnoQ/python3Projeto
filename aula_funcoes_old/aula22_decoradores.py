"""
Aprender a criar funções decoradoras e decoradas
@static por exemplo
"""


def maas(funcao):
    def slave(*args, **kwargs):
        print('Estou decorada baby!')
        funcao(*args, **kwargs)  # Adicionando o () digo para o interpretador que isso é uma função! Tipagem dinâmica
        # mata!

    return slave


# PQP aí já demais, função decorada! TOPPP
@maas
def fala_oi():
    print('Oi')


@maas
def outra_funcao(msg):
    print(msg)


# Decorada na "mão"
# fala_oi = master(fala_oi)  # Variavel é uma função

fala_oi()
outra_funcao('Ola senhorsesa')

"""
Problemas dos parâmetros mutáveis (LISTAS e DICIONARIOS por exemplo) em funções
"""


# o problema esta em lista , pois o interpretador do python cria uma UNICA LISTA na memória
# e sempre que o metodo for chamado com esse valor default, ela sera ALTERADA e nao um novo criado!
def lista_de_clientes(clientes_novos, lista=[]):
    lista.extend(clientes_novos)  # vai sempre engordando a mesma lista.
    return lista


clientes1 = lista_de_clientes(['MÁRCIA', 'ANA', 'FELIPA'])  # lista DEFAULT
clientes2 = lista_de_clientes(['ENRICA', 'LUCIA', 'VERA'])  # lista DEFAULT

print(clientes1)
print(clientes2)  # LISTA MERGEADA
