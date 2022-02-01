from copy import copy

"""
Dicionarios e TUPLAS
Nos Dicionários (MAP do java), defino o valor da chave
"""

t1 = 1, 2, 3, 4, 5
t2 = 6, 7, 8, 9, 10
t3 = t1 + t2
t4 = (1, 2, 3, 4, 5) * 10  # Vai repetir 10x
l1 = list(t1)  # Converter tupla para lista e modificar

print(t3)  # Concatenei tuplas
print(t4)  # Concatenei tuplas

"""
Dicionários
"""
d1 = {'chave1': 'valor da chave', 'chave2': 'valor da chave2'}
d2 = dict(chave1="valor da chave", chave2='Valor da chave')
d1['chave1'] = 'novo valor'
do = dict(key1="valora", key2='Valorz')
dz = d2.update(do)  # Concatenar dicts
del d2['chave2']
print(dz)
print(d2, d1, d1.get('chave1'))

for k, v in d1.items():
    print(k, v)

clientes = {
    'cliente1': {
        'nome': 'Maria',
        'sobrenome': 'Berma'
    },
    'cliente2': {
        'nome': 'Joana',
        'sobrenome': 'Berma'
    }
}

for key_cliente, value_cliente in clientes.items():
    print(f'Exibindo {key_cliente}')
    for dados_k, dados_v in value_cliente.items():
        print(f'\t{dados_k} = {dados_v}')

v = clientes.copy()  # Copia fake, cause altere os valores de v vai afetar o clientes também
z = copy(clientes)  # COpia boa

"""
Conjutos no pythos
Não respeitam ordem
Não da para acessar um elemento através de index
Somente elementos únicos
Lentos na inserção
add
updte
clear
discar
union '|'
intersection '&' (todos os elementos presentes nos dois sets)
difference '-' (elementos apenas no set da esquerda
symetric_difference '^' (Elementos que estão nos dois sets, mas não em ambos
"""
s1 = {1, 2, 'a'}
s2 = set()
s2.add(1)
s2.add(2)
s2.add(3)

sx = {1, 2, 3, 4, 5, 6, 7}
sy = {1, 2, 3, 4, 5, 6, }
sCompare = sx - sy
print(sCompare)
