def teacher():
    print("oi")


def pigeon(messenger, name):
    print(name, messenger)


def jaguar(messenger="Mensagem Default", name="Nome Default"):
    print(name, messenger)


teacher()
pigeon("Fogo na bomba", "Brunno")
jaguar()
jaguar(name='Zezinho')  # Com parâmetros nomeados é possível mudar a ordem de envio deles.


def send_print(var):
    print(f'send_print printou {var}')


def dumb():
    return send_print


var = dumb()

print(dumb()("Locura chamei outra função"))  # Isso acontece pois dumb retorna a função
print(id(var), id(dumb()), id(send_print))  # Mesmo endereço de memória


# TUPLA
def dumb2():
    return 'Brenda', 'Michelle'


print(type(dumb2()))

"""
Funções em Python - *args **kwargs
kwargs siginifica --> keyword arguments, e somente por convenção se chama assim, é representado por dois '**'
     args é representado por '*' *args **kwargs
"""


# args é UMA TUPLA
def dummy(*args, **kwargs):
    print(args)
    print(len(args))
    print(type(args))
    print(type(kwargs))
    if kwargs:
        print(kwargs['name'], kwargs['surname'])
        print(kwargs.get('nome'))  # Dessa maneira é melhor que nao tomo NULLPOINTER


dummy(1, 2, 3, 45, 6)
listU = [1, 5, 14, 48, 6]
dummy(listU)  # Lista sem DESEMPACOTAMENTO
dummy(*listU)  # Lista com DESEMPACOTAMENTO
dummy('Veransca', 'Rancher', 'Mandrião', 'servente', name='Brunno', surname='Silva')
