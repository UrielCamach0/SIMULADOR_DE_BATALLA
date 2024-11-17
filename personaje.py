# PERSONAJE

import random

class Personaje:
    def __init__(self, nombre, hp, ataque, defensa, pociones):
        self.nombre = nombre
        self.hp = hp
        self.ataque = ataque
        self.defensa = defensa
        self.pociones = pociones

    def atacar(self, otro_personaje):
        critico = random.choice([False] * 3 + [True])  # 25% de probabilidad de critico
        fallo = random.choice([False] * 3 + [True])    # 25% de probabilidad de fallo
        
        if fallo:
            print(f"{self.nombre} intenta atacar a {otro_personaje.nombre}, ¡pero falla!\n")
            return

        dano = random.randint(1, self.ataque)

        if critico:
            dano *= 2
            print(f"¡Golpe critico de {self.nombre}!")
        
        # Considerar la defensa del otro personaje
        dano = max(0, dano - otro_personaje.defensa)
        otro_personaje.hp -= dano
        otro_personaje.hp = max(0, otro_personaje.hp)  # Evita HP negativo

        print(f"{self.nombre} ataca a {otro_personaje.nombre} y causa {dano} puntos de daño.")
        print(f"{otro_personaje.nombre} ahora tiene {otro_personaje.hp} puntos de vida.\n")

    def usar_pocion(self):
        if self.pociones > 0:
            curacion = random.randint(15, 30)
            self.hp += curacion
            self.pociones -= 1
            print(f"{self.nombre} usa una pocion y recupera {curacion} puntos de vida.")
            print(f"{self.nombre} ahora tiene {self.hp} puntos de vida.\n")
        else:
            print(f"{self.nombre} intenta usar una pocion, ¡pero no le quedan!\n")

    def habilidad_especial(self, otro_personaje):
        dano = random.randint(self.ataque, self.ataque * 2)
        otro_personaje.hp -= dano
        otro_personaje.hp = max(0, otro_personaje.hp)
        print(f"{self.nombre} usa su habilidad especial y causa {dano} puntos de daño a {otro_personaje.nombre}.")
        print(f"{otro_personaje.nombre} ahora tiene {otro_personaje.hp} puntos de vida.\n")









