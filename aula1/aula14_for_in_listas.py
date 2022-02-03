"""
For in Python
Iterando strings com for
Função range(start=0, stop, step=1)
"""
texto = "Python"
lista = ['A', 'B', 'C']

for a in texto:
    print(a)

for n in range(0, 10, 2):
    print(n)

lista.append('Romeu')
lista.insert(0, 'OLGA')

print('EIII', lista.index('OLGA'))

for xa in lista:
    print(xa)

"""
For / Else em python
"""
names = ['Maria', 'Ursula', 'Beti']

for n in names:
    if n.startswith('M'):
        print(f'Este nome, {n}, começa com "M"')
        break
else:
    print('Nenhum nome começa com "M"')

"""
Split, Join, Enumerate em Ptyhon
* Split - Quebrar a string por determinado padrão
* join - Juntar uma lista em uma STRING
* Enumerate - enumerar elementos da lista
"""
phrase = 'O Brasil é o o pais do futebol, o Brasil é penta.!'
split1 = phrase.split(" ")
split2 = phrase.split(",")

word_that_most_appeared = ''
counter = 0
print(f'Veja como ficou {split1}')

print(f'Veja como ficou 2 {split2}')

for w in split1:
    quantity_times = split1.count(w)

    if quantity_times > counter:
        counter = quantity_times
        word_that_most_appeared = w

print(f'A palavra que mais apareceu foi; "{word_that_most_appeared}" "{counter}" vezes.')
# JOIN
another_message = ' '.join(split1)
print(another_message)

# Enumerate
for index, value in enumerate(phrase):
    print(f'Indice {index} e valor {value}')

"""
Desempacomento em PYTHON
O *_ é uma convenção e indica para outros desenvolvedores de python que esta variavel 
não será mais utilizada em outros trechos do programa.
"""
names2 = ['Hugo', 'Chico Bento', 'Monica', 'Cebolinha', 'Zacarias', 'Maria', 'Barbara']
n1, n2, *_ = names2
n3, n4, *remainder_of_list = names2
print(n1, n2, *_)
print(n3, n4, *remainder_of_list)  # Que loucura bicho!
# Que loucura bicho, nesse tipo de desempacotamento os utlimos elementos são obtidos primeiro
*remainder_of_list2, n5, n6,  = names2
print(n5, n6, *remainder_of_list2)
