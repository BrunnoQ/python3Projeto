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
