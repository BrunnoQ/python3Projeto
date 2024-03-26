from random import randint

"""
Trocando valores de variáveis em PYTHON!
Trocar valores de variaveis sem muitas linhas de código
"""
#  TOP demais, vantagem de linguagem com tipagem dinaminca
x = 'SIMONE'
z = 36
y = 'Stella'
z, y, x = x, z, y
print(f'Valores trocados, {x}, {z}, {y}')  # ANIMAL! SENSACIONAL!

"""
Operador ternário
"""
logged_user = True
msg = 'Usuário logado' if logged_user else 'Usuário deve logar no sistema!'
print(msg)

"""
Usando OR de maneira SIMPLES!!!
Menos código escrito
"""
namex = input("Qual seu nome camarada? ")
print(namex or 'Fale seu nome camarada!')

"""
Contador simples
Um progressivo e outro regressivo
"""

for p, r in enumerate(range(10, 1, -1)):
    print(p, r)

"""
Validador de CPF basicão
"""
cpf = '16899535009'
new_cpf = cpf[:-2]
reverse = 10
total = 0

for index in range(19):
    if index > 8:
        index -= 9

    total += int(new_cpf[index]) * reverse

    reverse -= 1
    if reverse < 2:
        reverse = 11
        d = 11 - (total % 11)

        if d > 9:
            d = 0
        total = 0
        new_cpf += str(d)

print(new_cpf)

"""
Gerador de CPF basico
"""

cpf = str(randint(100000000, 999999999))
new_cpf = cpf
reverse = 10
total = 0

for index in range(19):
    if index > 8:
        index -= 9

    total += int(new_cpf[index]) * reverse

    reverse -= 1
    if reverse < 2:
        reverse = 11
        d = 11 - (total % 11)

        if d > 9:
            d = 0
        total = 0
        new_cpf += str(d)

print(new_cpf)
