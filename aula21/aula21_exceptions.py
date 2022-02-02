
try:
    a = []
    print(a[1])
except NameError as erro:
    print('Erro:', erro)
except (IndexError, KeyError) as erro:
    print('Chora menino', erro)
except Exception as erro:
    print('Erro nao mapeado', erro)
else:
    print('Executou o código com sucesso!')
finally:
    print("Sempre fecha")


def divide(n1, n2):
    try:
        return n1 / n2
    except ZeroDivisionError:
        raise ValueError('N2 não pode ser ZERO!')


print(divide(23, 0))
