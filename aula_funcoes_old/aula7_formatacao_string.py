"""
Utilizando o F STRINGS
"""
name = "Brunno Silva"
age = 35
height = 1.83
is_of_age = age > 18
weight = 86
imc = weight / height ** 2

print(name, "tem", age, "de idade e seu imc é", imc)
print(f'{name} tem {age} de idade e seu imc é {imc:.2f}')  # coisa linda!!!!
print('{} tem {} de idade e seu imc é {}'.format(name, age, imc))
# Denifindo alias para variaveis posso repetir variaveis sem respeitar ordens!
print('{xota} tem {x} de idade e seu imc é {z:.2f}'.format(xota=name, x=age, z=imc))
print("tipo name", type(name))
print("tipo age", type(age))
print("tipo height", type(height))
print("tipo is_of_age", type(is_of_age))
print("tipo weight", type(weight))
print("tipo imc", type(imc))
