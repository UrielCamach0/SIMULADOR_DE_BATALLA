# MAIN

from personaje import Personaje
from simulador import SimuladorBatalla

# Creación de personajes
personaje1 = Personaje("Guerrero", hp=120, ataque=25, defensa=10, pociones=2)
personaje2 = Personaje("Mago", hp=90, ataque=30, defensa=5, pociones=3)

# Iniciar la simulacion
batalla = SimuladorBatalla(personaje1, personaje2)
batalla.simular()
