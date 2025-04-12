import random
import time

race =  {  "enano": {"vida": 120, "fuerza": 8, "defensa": 10},
                "elfo": {"vida": 100, "fuerza": 10, "defensa": 6},
                "hombre": {"vida": 110, "fuerza": 9, "defensa": 8}
}



class Enemigo:
          def __init__(self, nombre, vida, fuerza):
              self.nombre = nombre
              self.vida = vida
              self.fuerza = fuerza

          def atacar(self):
              return random.randint(1, self.fuerza)

          def mostrar(self):
              print(f"\n¡Un {self.nombre} aparece! Vida: {self.vida}, Fuerza: {self.fuerza}")

class Goblin(Enemigo):
          def __init__(self):
              super().__init__("Goblin", vida=20, fuerza=5)

class CriaturaDelLodo(Enemigo):
          def __init__(self):
              super().__init__("Criatura del Lodo", vida=35, fuerza=8)

class GuardianDeLaMazmorra(Enemigo):
          def __init__(self):
              super().__init__("Guardián de la Mazmorra", vida=50, fuerza=12)
def trampa(jugador):
          print("\n¡Has activado una trampa!")

          try:
              eleccion = int(input("Rápido, elige un número del 1 al 10 para intentar esquivarla: "))
              if eleccion < 1 or eleccion > 10:
                  print("Número fuera de rango. No logras reaccionar a tiempo.")
                  eleccion = -1  # Fuerza un fallo
          except ValueError:
              print("¡Eso no era un número válido! Tropiezas directamente con la trampa.")
              eleccion = -1

          numero_secreto = random.randint(1, 10)

          if eleccion == numero_secreto:
              print("\033[92m¡Has esquivado la trampa con éxito!\033[0m")
          else:
              daño = random.randint(5, 15)
              jugador.vida -= daño
              print(f"\033[91m¡La trampa se activa! Pierdes {daño} de vida.\033[0m Vida restante: {jugador.vida}")


class jugador:
          def __init__(self, nombre, raza, vida, fuerza, defensa):
              self.nombre = nombre
              self.raza = raza
              self.vida = race[vida]["vida"]
              self.fuerza = race[fuerza]["fuerza"]
              self.defensa = race[defensa]["defensa"]

          def atacar(self):
              return self.fuerza

          def recibir_daño(self, daño):
              daño_real = max(0, daño - self.defensa)
              self.vida -= daño_real
              return daño_real

          def esta_vivo(self):
              return self.vida > 0

          def mostrar_stats(self):
              print(f"{self.nombre} el {self.raza.capitalize()} - Vida: {self.vida}, Fuerza: {self.fuerza}, Defensa: {self.defensa}")
def combate(jugador):
          Enemigos_posibles = [Goblin(), CriaturaDelLodo(), GuardianDeLaMazmorra()]
          Enemigo = random.choice(Enemigos_posibles)
          Enemigo.mostrar()
          print("¡Prepárate para luchar!")

          while Enemigo.vida > 0 and jugador.vida > 0:
      # Turno del jugador
              daño_jugador = jugador.atacar()
              Enemigo.vida -= daño_jugador
              print(f"\nAtacas al {Enemigo.nombre} y le haces {daño_jugador} de daño. Vida del Enemigo: {Enemigo.vida}")

              if Enemigo.vida <= 0:
                  print(f"\n¡Has derrotado al {Enemigo.nombre}!")
                  return

      # Turno del Enemigo
              daño_Enemigo = Enemigo.atacar()
              daño_recibido = jugador.recibir_daño(daño_Enemigo)
              print(f"El {Enemigo.nombre} te ataca y te hace {daño_recibido} de daño. Tu vida: {jugador.vida}")
              time.sleep(1)

          if not jugador.esta_vivo():
              print(f"\nEl {Enemigo.nombre} te ha derrotado...")

def camino_tranquilo(jugador):
     print("caca")
# Por definir
def choose_action(): #a medias
    while True:
        decision = input ("¿Qué quieres hacer? ¿Avanzar o esperar?")
        if decision.lower() == "avanzar":
            print("Avanzas")#llamar funcion para la primera cueva
            break
        elif decision.lower() == "esperar":
            print("Esperando...")
            time.sleep(1)
            print("Nada sucede.")
            time.sleep(1)
            continue

def select_race(): #Pregunta raza

    while True:
        
        raza = input("\033[34m¿Qué raza quieres ser? ¿Enano, elfo u Hombre?:  \033[m").lower()
        
        time.sleep(1)
        if raza in race:
            stats = race[raza]
            print("\033[31m¡Estupendo!\033[0m")
            time.sleep(2)
            print(f"\n¡Bienvenido, {name} el {raza.capitalize()}!")
            time.sleep(1)
            print(f"Tus estadísticas son: Vida: {stats['vida']}, Fuerza: {stats['fuerza']}, Defensa: {stats['defensa']}")
            break  # Salimos del bucle cuando se elige una raza válida
        else:
            print("\nRaza no válida. Elige entre enano, elfo o hombre.")
            continue

def doors():
     how_many_doors = random.randint(1, 5)
     print("Tienes",how_many_doors,"puertas ante ti.")
     choose_door = input("¿Cuál eliges?")      
    
    
print("Cargando", end="", flush=True)
for _ in range(4):
    time.sleep(0.75)
    print(".", end="", flush=True)
print()  

caption_intro = "\033[31mBienvenido a la mazmorra de Python\n \033[0m"
for letra in caption_intro:
    print(letra, end="", flush=True)
    time.sleep(0.02)
time.sleep(0.5)
caption_choose_race = "\033[34mElige tu nombre y raza. ¡Prepárate para la aventura!\033[0m\n"
for letra in caption_choose_race:
    print(letra, end="", flush=True)
    time.sleep(0.03)

name= input("¿Cómo deberían llamarte?: ")
time.sleep(1)
print("¡Un gran nombre!")
time.sleep(2)
print("¡Bien! Vamos allá...")
time.sleep(1)

select_race()

user = jugador(name, raza, race[raza]["vida"], raza, raza)
# caption_intro1 = """\033[32mNotas una helada brisa en la nuca, arrugas los ojos y parpadeas con esfuerzo. Te levantas, la cabeza te da vueltas como si te hubieran golpeado.
# Luchas por ver frente a ti, esta oscuro; increiblemente oscuro. Consigues ver algo cerca tuya. ¿Que es...?\033[0m
# \033[33mPor fin despiertas\033[0m \033[32m---Escuchas y meneas la cabeza.\033[0m
# \033[33m¿Donde estoy?\033[0m \033[32m--susurras. \033[0m
# \033[33mEstamos atrapados. \033[0m \033[32m--dice la silueta. No reconoces... esa voz.\033[0m"""
# for letra in caption_intro1:
#     print(letra, end="", flush=True)
#     time.sleep(0.02)

print()
print()

doors()

combate(user)