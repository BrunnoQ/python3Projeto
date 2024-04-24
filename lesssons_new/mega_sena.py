import random
import ephem

def mega_sena():
    """
    Gera um jogo para a mega sena
    """
    return [random.randint(1, 60) for _ in range(6)]

def get_moon_phase(day):
    moon = ephem.Moon()
    moon.compute(day)
    return moon.phase

# Use a função assim:
print(get_moon_phase('2024/04/23'))  # Substitua pela data desejada
print(mega_sena())