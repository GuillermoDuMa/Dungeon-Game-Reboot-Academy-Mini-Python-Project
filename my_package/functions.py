import random
import time
from classes import Goblin, CriaturaDelLodo, GuardianDeLaMazmorra, race
from main import name
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

def combate(jugador):
          enemigos_posibles = [Goblin(), CriaturaDelLodo(), GuardianDeLaMazmorra()]
          enemigo = random.choice(enemigos_posibles)
          enemigo.mostrar()
          print("¡Prepárate para luchar!")

          while enemigo.vida > 0 and jugador.esta_vivo():
      # Turno del jugador
              daño_jugador = jugador.atacar()
              enemigo.vida -= daño_jugador
              print(f"\nAtacas al {enemigo.nombre} y le haces {daño_jugador} de daño. Vida del enemigo: {enemigo.vida}")

              if enemigo.vida <= 0:
                  print(f"\n¡Has derrotado al {enemigo.nombre}!")
                  return

      # Turno del enemigo
              daño_enemigo = enemigo.atacar()
              daño_recibido = jugador.recibir_daño(daño_enemigo)
              print(f"El {enemigo.nombre} te ataca y te hace {daño_recibido} de daño. Tu vida: {jugador.vida}")
              time.sleep(1)

          if not jugador.esta_vivo():
              print(f"\nEl {enemigo.nombre} te ha derrotado...")

def camino_tranquilo(jugador):
     print("caca")
# Por definir


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
 

print("¡Este es el functions.py correcto!")
