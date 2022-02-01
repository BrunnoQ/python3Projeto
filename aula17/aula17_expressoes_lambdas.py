"""
Lambdas são funções anonima, pois, não possuem nomes!
Usado para quando precisar outra função como parâmetro
"""


def mult(arg1, arg2):
    return arg1 * arg2


a = lambda arg1, arg2: arg1 * arg2  # Mesma coisa que a função de cima!

print(a(2, 3))
# Exemplo de uso , definido chave de ordenação para lista

products = [
    ['P1', 30],
    ['P2', 100],
    ['P3', 40],
    ['P3', 70],
    ['P5', 70]
]
print(sorted(products, key=lambda item: item[1], reverse=True))  # Ordernar por preço SEM ALTERAR a ORIGINAL
products.sort(key=lambda item: item[1])
print(products)  # Ordernar por preço
