"""
Entrada de dados para o usuário destruir o sistema
"""
import datetime

name = input("Qual teu nome camarada? \n")
print(f'O nome do usuário é {name} e o tipo da variavel é', type(name))
age = input("Qual tua idade camarada? \n")
print(f'O nome do usuário é {name} e sua idade é {age}')
birth_year = 2022 - int(age)
print(f'Ano de nascimento é {birth_year}.')
