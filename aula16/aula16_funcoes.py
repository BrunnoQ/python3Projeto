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

#TUPLA
def dumb2():
    return 'Brenda', 'Michelle'


print(type(dumb2()))
