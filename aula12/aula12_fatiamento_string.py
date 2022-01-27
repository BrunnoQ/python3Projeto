"""
* Fatiamento de string [inicio:fim:passo]
Funções built-in len, abs, type, prin e etc
Maiores detalhes conferir a documentação
"""
# positivos
text = 'Brunno Silva'
print(text[2])
print(text[2:6])  # fatiamento o 6 não é incluindo
print(text[:6])  # Sem informar o inicio e dizendo só o fim
print(text[6:])  # Sem informar o fim e dizendo só o começo
# negatives Remove elementos da busca
print(text[-12:7])  # Remove elementos da busca
# fazer busca pulando caracteres
print(text[0:7:2])  # pulando de 2 em dois caracteres
