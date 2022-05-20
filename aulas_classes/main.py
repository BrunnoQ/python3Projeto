from pessoa import Pessoa

p1 = Pessoa(nome='Carla', idade=26)
p1.comer('Amoraw')
p1.comer('Amora')

print(Pessoa.ano_atual)
print(p1.get_ano_nascimento())
p2 = Pessoa.por_ano_nacimento('Ramon', 1986)
print(type(p2))
print(Pessoa.por_ano_nacimento('Ramon', 1986))
print(f'Gerando ID {Pessoa.gera_id()}')
p3 = Pessoa('Gertrudes', '1986')
print(f'IDade {p3.idade}')
