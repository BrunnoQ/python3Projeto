"""
Verificar se o número é impar ou par
"""
number = input('Informe um número inteiro camarada: ')

if number.isnumeric():
    if int(number) % 2 == 0:
        print("O número é par camarada!")
    else:
        print("O número é ímpar camarada!")
else:
    print('Eu disse um número INTEIRO camarada!')

"""
Faça o sistema saudar conforme horario
"""
hour = input('Que horas são camarada?: ')

if hour.isnumeric():
    hour_convert = int(hour)
    if 0 <= hour_convert <= 11:
        print('Bom dia, camarada!')
    elif 12 <= hour_convert <= 17:
        print('Boa tarde camarada!')
    else:
        print('Boa noite camarada!')
else:
    print("Informe apenas a hora cheia camarada!")