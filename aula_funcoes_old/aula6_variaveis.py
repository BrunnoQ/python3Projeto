"""
Devem iniciar com letra, pode conter numeros, separar com '_', letra minusculas
"""
NAME = "Brunno Silva"
AGE = 35
ALTURA = 1.83
IS_OF_AGE = AGE > 18
PESO = 86
IMC = PESO / ALTURA ** 2

print(NAME, "tem", AGE, "de idade e seu imc é", IMC)
print("tipo name", type(NAME))
print("tipo age", type(AGE))
print("tipo height", type(ALTURA))
print("tipo is_of_age", type(IS_OF_AGE))
print("tipo weight", type(PESO))
print("tipo imc", type(IMC))
