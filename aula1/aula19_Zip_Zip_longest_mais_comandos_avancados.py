from itertools import zip_longest, count, combinations, permutations, product, groupby
from functools import reduce
from types import GeneratorType

"""
Zip - Unindo iterávies
Zip_longest - Itertools
"""

### Código
cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo']

estados = ['SP', 'MG', 'BA']
contador = count()
# Python eh vida , aqui retornou um ITERADOR, essa cara so mergea ate a menor lista! no caso ESTADOS
cidades_Estados = zip(contador, estados, cidades)

cidades_Estados2 = zip_longest(estados, cidades, fillvalue='EstadoDefault')

print(list(cidades_Estados))
print(list(cidades_Estados2))
for valor in cidades_Estados:
    print(valor)
# Contadores
contador = count(start=0, step=1)

"""
Que linguagem do caRAI: 
Combinations, Permutations e Product - Itertools
Combinação - Ordem não importa
Permutação - Ordem importa
Ambos não repetem valores únicos
Produto - Ordem importa e repete valores únicos
"""
pessoas = ['Flávia', 'Márcia', 'André', 'Leticia', 'Ina', 'Paula']

for grupo in combinations(pessoas, 2):
    print(grupo)

for grupo in permutations(pessoas, 2):
    print(grupo)

for grupo in product(pessoas, repeat=2):
    print(grupo)

"""
Group BY
Precisa estar ordenado
"""
alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Romena', 'nota': 'C'},
    {'nome': 'Zelda', 'nota': 'A'},
    {'nome': 'Lichia', 'nota': 'C'},
    {'nome': 'Romero', 'nota': 'B'},
    {'nome': 'Istia', 'nota': 'D'},
    {'nome': 'Istia', 'nota': 'D'},
    {'nome': 'Rica', 'nota': 'C'},
]
ordena = lambda item: item['nota']
alunos.sort(key=ordena)
alunos_agrupados = groupby(alunos, ordena)

for nota, valores_agupados in alunos_agrupados:
    print(f'NOTA {nota}')
    for z in valores_agupados:
        print(z)

"""
MAP
"""
produtos = [
    {'nome': 'p1', 'preco': 20.55},
    {'nome': 'p2', 'preco': 12.36},
    {'nome': 'p3', 'preco': 14},
    {'nome': 'p4', 'preco': 36.50},
    {'nome': 'p5', 'preco': 70.50},
    {'nome': 'p6', 'preco': 80.56},
    {'nome': 'p7', 'preco': 1.56},
    {'nome': 'p8', 'preco': 1.55},
]

clientes = [
    {'nome': 'Romena', 'idade': 10},
    {'nome': 'Laura', 'idade': 35},
    {'nome': 'Zema', 'idade': 45},
    {'nome': 'Arthur', 'idade': 57},
    {'nome': 'Bob', 'idade': 40},
    {'nome': 'Lorena', 'idade': 66},
    {'nome': 'Cintia', 'idade': 59},
    {'nome': 'Marena', 'idade': 40}
]

ops = [1, 2, 3, 4, 5, 6, 7, 8]

nova_lista = map(lambda x: x * 2, ops)  # mesma coisa se não quiser usar compreensions
nova_lista2 = [x * 2 for x in ops]
print(list(nova_lista))
print(nova_lista2)

"""
Filter
"""
lista_filtrada = filter(lambda x: x > 2, ops)
print(list(lista_filtrada))
produtos_filtrados = filter(lambda p: p.get('preco') > 10.50, produtos)
for pro in produtos_filtrados:
    print(pro)

"""
REduce
"""
lista_somada = reduce(lambda ac, i: i + ac, ops, 0)
print(lista_somada)
produtos_somados = reduce(lambda ac, p: p.get('preco') + ac, produtos, 0)
print(produtos_somados)
