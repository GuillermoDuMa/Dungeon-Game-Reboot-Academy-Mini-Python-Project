# Dungeon-Game-Reboot-Academy-Mini-Python-Project

## Escape de la mazmorra 

proyecto conjunto ente @GuillermoDuMa y @CiaraBootcamp
### Requisitos iniciales proyecto: 

DungeonEscape_Basic:
● Descripción: Juego de texto donde el jugador debe escapar de una mazmorra  
eligiendo entre diferentes caminos.  
● Decisiones: Ofrecer varias opciones en cada cruce.  
● Resultado: Algunas decisiones llevan a trampas, otras permiten avanzar  

## Descripción solución:

El juego iniciará solicitando al jugador elegir un nombre y una de las tres razas disponibles para el héroe:

          chosen_race =  {
                        "dwarf": {"health": 120, "strength": 8, "defence": 10},
                        "elf": {"health": 100, "strength": 10, "defence": 6},
                        "human": {"health": 110, "strength": 9, "defence": 8}
                         } 

Posteriormente el jugador tendrá que elegir entre una serie de puertas para iniciar la aventura, y a partir de aqui, el juego se desarrollará en un bucle FOR de 5 iteraciones. 

La puerta elegida generará un evento de entre los siguientes:

● ELegir puerta: Todos los eventos iran precedidos por una elección de una puerta.

          def doors():
              how_many_doors = random.randint(1, 5)
    
              print("Tienes",how_many_doors,"puertas ante ti.")
              while True:
                  try:
                      choose_door = int(input("¿Cuál eliges?: "))
                  except ValueError:
                      print("No es un número válido. Intenta de nuevo.")
                      continue
                  if choose_door < 1 or choose_door > how_many_doors:
                      print("No existe esa puerta, zopenco! Elige sabiamente")
                      continue
                  else:
                      break
           print(f"has elegido la puerta {choose_door} buena suerte aventurero")


● Trampa:
Una trampa se activará cuando el jugador avanza y tendrá la posibilidad de esquivarla mediante una mecánica de elección de un número del 1 al 10. Si el numero coincide con el numero que se generará aleatoriamente, logrará esquivar la trampa. Si no, recibirá daño y la aventura continuará. Habrá tambien interacciones con el npc aliado con el que contará el jugador.

          def trap(protagonist):
          print("\n¡Has activado una trampa!")

          try:
              choice = int(input("Rápido, elige un número del 1 al 10 para intentar esquivarla: "))
              if choice < 1 or choice > 10:
                  print("Número fuera de rango. No logras reaccionar a tiempo.")
                  choice = -1  # Fuerza un fallo
          except ValueError:
              print("¡Eso no era un número válido! Tropiezas directamente con la trap.")
              choice = -1

          secret_number = random.randint(1, 10)

          if choice == secret_number:
              print("\033[92m¡Has esquivado la trap con éxito!\033[0m")
          else:
              damage = random.randint(5, 15)
              protagonist.health -= damage
              print(f"\033[91m¡La trap se activa! Pierdes {damage} de health.\033[0m Vida restante: {protagonist.health}")

● Combate: 
El jugador se topará con un enemigo al que tendrá que batir para poder continuar.

          def combat(protagonist):
          possible_enemies = [Goblin(), Abyss_creature(), Dungeon_boss()]
          enemy = random.choice(possible_enemies)
          enemy.Appear()
          print("¡Prepárate para luchar!")

          while enemy.health > 0 and protagonist.is_alive():
      # Turno del protagonista
              protagonist_damage = protagonist.attack()
              enemy.health -= protagonist_damage
              print(f"\nAtacas al {enemy.name} y le haces {protagonist_damage} de daño. Vida del Enemy: {enemy.health}")

              if enemy.health <= 0:
                  print(f"\n¡Has derrotado al {enemy.name}!")
                  return
      # Turno del Enemigo
              enemy_damage = enemy.strength
              damage_taken = protagonist.take_damage(enemy_damage)
              print(f"El {enemy.name} te ataca y te hace {damage_taken} de daño. Tu health: {protagonist.health}")
              time.sleep(1)

          if not protagonist.is_alive():
              print(f"\nEl {enemy.name} te ha derrotado...")


● Cueva/camino tranquilo:
El jugador no encontrará obstáculos. Estos tramos se aprovecharán para dar contexto a la historia y ofrecer descripciones del lugar y dar pie a diaologos con el npc aliado.

          def quiet_advance(protagonist):
    path_random = {'path1':"Continuas tu camino por la oscura y húmeda mazmorra. La sensación de desamparo te abruma, pero debes seguir adelante.", 
    'path2':"No sé como hemos llegado aquí ni por qué, pero algo me dice que esto es obra del destino. -Dice tu compañero mientras cruzáis el umbral",
    'path4': "Notas una ligera brisa de aire desde más adelante. Si la salida está ahí, merecerá la pena continuar sea lo que sea que enfrentes",
    'path5': "Pisas un charco de agua. ¡Agua! Aprovechas y bebes. Tu compañero te mira con recelo. ¿Será potable? Aun así, estás muerto de sed.",
    'path6': 'Detectas rastros de sangre por el suelo y las paredes... --se han cometido atrocidades aquí. --dices entre murmullos.',
    'path7': 'Vaya ánimos que me traes compañero. Debemos salir de aquí antes de que se percaten de que hemos escapado de la celda.'
    } 
    path = random.choice(list(path_random.values()))
    return path 
    
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
