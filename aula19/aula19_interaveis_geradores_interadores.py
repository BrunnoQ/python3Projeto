import sys
import time

"""
Iteraveis - Lista
Iterador - FOR WHILE
INTERADORES - tem o hasNext 
Geradores - gera o proximo valor da lista
"""

lista = list(range(1000))
print(sys.getsizeof(lista))  # valor em bytes
print(hasattr(lista, '__next__'))  # Equivalente ao hasNext
x = iter(lista)  # virou um interador
print(x)


# Realiza o append de valores esperando 1 segundo a cada interação! EAGER - Retunr
def gera():
    r = []
    for i in range(100):
        r.append(i)
        time.sleep(0.1)  # 1 segundo
    return r


# Retorna 1 elemento assim que estiver na lista! Lazy - Return - Eis um gerador
# Muito louco!! poupaa memória
def gera2():
    r = []
    for i in range(100):
        yield i
        time.sleep(0.1)  # 1 segundo


# g = gera()
g2 = gera2()

for xpt in g2:
    print(xpt)

l1 = [x for x in range(10000)]
l2 = (x for x in range(10000))  # Outra forma de gerar um gerador
print(sys.getsizeof(l1))
print(sys.getsizeof(l2))  # BEM menos memória PQP! Isso acontece pois o valor só é alocado na memória quando solicitado!
