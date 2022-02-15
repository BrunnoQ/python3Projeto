from endereco import Endereco
from cliente import Cliente
from datetime import date

endereco1 = Endereco('Rua Curupireira', '03980-090', 247, 'São Paulo', 'SP')
cliente = Cliente('brunno', date.fromisoformat('1988-02-15'), endereco1)
print(endereco1)
print(cliente)

print(type(cliente.data_nascimento))
print(type(cliente.endereco))
print(cliente.obter_idade())
