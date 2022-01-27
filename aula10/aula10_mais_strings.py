user = input('Qual teu nome camarada? \n')
quantity_characters = len(user)

if quantity_characters <= 10:
    print("Não economize nos caracteres camarada!, informe ao menos 10 letras!")
else:
    print("Você foi armazenado com sucesso camarada!")

# Checagens básicas
num1 = input("Digite um numero camarada: ")
num2 = input("Digite outro numero camarada: ")

# Ler documentação só valida numeros positivos e nao flutuantes!
if num1.isnumeric() and num2.isnumeric():
    print(f'A soma de {num1} e {num2} é:', int(num2) + int(num1), 'camarada!')
else:
    print('Informe somente números inteiros camarada!')
