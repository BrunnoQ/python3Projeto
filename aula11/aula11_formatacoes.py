"""
Formatando valores com modificadores
:s - Texto (strings)
:d - Inteiros (int)
:f - Números de ponto flutuante (float)
:.(número)f - quantidade de casas decimais
:(CARACTER) (> ou < ou ^) Quantidade)
> - Esquerda
< - Direita
^ - Centro
"""
number1 = 10
number2 = 3
division = 10 / 3
name = 'Brunno Silva'

print(f'{name:s}')
print(f'{division}')
print(f'{division:.2f}')  # Exibir 2 casas decimais
print(f'{division:.4f}')  # Exibir 4 casas decimais
print(f'{number1:0<10}')  # Number deve conter 10 casas adicionando zeros a DIREITA
print(f'{number1:0>10}')  # Number deve conter 10 casas adicionando zeros a ESQUERDA
print(f'{name:X^100}')  # Adicionando BRUNNO AO CENTRO de X
