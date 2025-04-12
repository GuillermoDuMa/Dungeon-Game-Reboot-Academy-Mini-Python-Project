# Dungeon-Game-Reboot-Academy-Mini-Python-Project

## Escape de la mazmorra 

proyecto conjunto ente @GuillermoDuMa y @Ciara
### Requisitos iniciales proyecto: 

DungeonEscape_Basic:
● Descripción: Juego de texto donde el jugador debe escapar de una mazmorra  
eligiendo entre diferentes caminos.  
● Decisiones: Ofrecer varias opciones en cada cruce.  
● Resultado: Algunas decisiones llevan a trampas, otras permiten avanzar  

## Descripción solución:

El juego iniciará solicitando al jugador elegir un nombre y una de las tres razas disponibles para el héroe:

          raza =  {  "enano": {"vida": 120, "fuerza": 8, "defensa": 10},
                    "elfo": {"vida": 100, "fuerza": 10, "defensa": 6},
                    "hombre": {"vida": 110, "fuerza": 9, "defensa": 8
                  }

Posteriormente el jugador tendrá que elegir entre una serie de puertas para iniciar la aventura, y a partir de aqui, el juego se desarrollará en un bucle FOR de 5 iteraciones. 

La puerta elegida generará un evento de entre los siguientes:

● Trampa:
Una trampa se activará cuando el jugador avanza y tendrá la posibilidad de esquivarla mediante una mecánica de elección de un número del 1 al 10. Si el numero coincide con el numero que se generará aleatoriamente, logrará esquivar la trampa. Si no, recibirá daño y la aventura continuará. Habrá tambien interacciones con el npc aliado con el que contará el jugador.

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

          # Cómo llamarla desde el flujo principal: 

          # trampa(jugador)

● Combate: 
El jugador se topará con un enemigo al que tendrá que batir para poder continuar.

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


● Cueva/camino tranquilo:
El jugador no encontrará obstáculos. Estos tramos se aprovecharán para dar contexto a la historia y ofrecer descripciones del lugar y dar pie a diaologos con el npc aliado.

    def camino_tranquilo(jugador):
    # Por definir
    
y a partir de aquí, una función random generará los siguientes eventos a ocurrir, de entre los anteriormente descritos.

### Acciones del jugador:

El jugador estará integrado en el código mediante una clase:

A lo largo del juego, el jugador podrá realizar las siguientes acciones:
● Elegir camino inicial.
● Combatir.
● Elegir numero del 1 al 10 para esquivar trampa.

Todo esto se integrará dentro de la clase Jugador:

          class Jugador:
              def __init__(self, nombre, raza):
                  self.nombre = nombre
                  self.raza = raza
                  self.vida = race[raza]["vida"]
                  self.fuerza = race[raza]["fuerza"]
                  self.defensa = race[raza]["defensa"]

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
 
### Enemigos 

Los enemigos se clasificarán en nivel de dificultad fácil, intermedia y difícil:

          class Enemigo:
              def __init__(self, nombre, vida, fuerza):
                  self.nombre = nombre
                  self.vida = vida
                  self.fuerza = fuerza

              def atacar(self):
                  return random.randint(1, self.fuerza)

              def mostrar(self):
                  print(f"\n¡Un {self.nombre} aparece! Vida: {self.vida}, Fuerza: {self.fuerza}")

● ENEMIGO DIFICULTAD FACIL:

          class Goblin(Enemigo):
              def __init__(self):
                  super().__init__("Goblin", vida=20, fuerza=5)

● ENEMIGO DIFICULTAD INTERMEDIA: 

          class CriaturaDelLodo(Enemigo):
              def __init__(self):
                  super().__init__("Criatura del Lodo", vida=35, fuerza=8)

● ENEMIGO DIFICULTAD DIFICIL:

          class GuardianDeLaMazmorra(Enemigo):
              def __init__(self):
                  super().__init__("Guardián de la Mazmorra", vida=50, fuerza=12)






