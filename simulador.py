# SIMULADOR

import random
from personaje import Personaje

class SimuladorBatalla:
    def __init__(self, personaje1, personaje2):
        self.personaje1 = personaje1
        self.personaje2 = personaje2

    def simular(self):
        print("¡Comienza la batalla!\n")
        turno = 1
        while self.personaje1.hp > 0 and self.personaje2.hp > 0:
            print(f"--- Turno {turno} ---")
            
            # Alternar turnos
            if turno % 2 != 0:
                self.turno_personaje(self.personaje1, self.personaje2)
            else:
                self.turno_personaje(self.personaje2, self.personaje1)
            
            turno += 1

        # Determinar el ganador
        if self.personaje1.hp <= 0 and self.personaje2.hp <= 0:
            print("\n¡Es un empate! Ambos personajes han caido.")
        elif self.personaje1.hp <= 0:
            print(f"\n{self.personaje2.nombre} ha ganado la batalla.")
        else:
            print(f"\n{self.personaje1.nombre} ha ganado la batalla.")

    def turno_personaje(self, atacante, defensor):
        accion = random.choice(["atacar", "pocion", "habilidad"])
        
        if accion == "atacar":
            atacante.atacar(defensor)
        elif accion == "pocion":
            atacante.usar_pocion()
        elif accion == "habilidad":
            atacante.habilidad_especial(defensor)
