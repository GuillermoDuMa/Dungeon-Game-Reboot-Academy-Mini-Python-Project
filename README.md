# Dungeon-Game-Reboot-Academy-Mini-Python-Project

![ChatGPT Image Apr 14, 2025, 03_45_20 PM](https://github.com/user-attachments/assets/0b225f6a-e772-48a1-80da-34364f5b71ed)


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
              "dwarf": {"health": 125, "strength": 10, "defence": 9},
              "elf": {"health": 90, "strength": 20, "defence": 6},
              "human": {"health": 110, "strength": 15, "defence": 8}
                  }

Posteriormente el jugador tendrá que elegir entre una serie de puertas para iniciar la aventura, y a partir de aqui, el juego se desarrollará en un bucle FOR de 5 iteraciones. 

La puerta elegida generará un evento de entre los siguientes:

● ELegir puerta: Todos los eventos iran precedidos por una elección de una puerta.

          def doors():
              how_many_doors = random.randint(2, 5)
              caption7 = ("\033[34mTienes ",how_many_doors," puertas ante ti.\033[0m\n")
              for word in caption7:
                  print(word, end="", flush=True)
              time.sleep(0.02)
              while True:
                  try:
                      choose_door = int(input("¿Cuál eliges?: "))
                  except ValueError:
                      print("No es un número válido. Intenta de nuevo.")
                      continue
                  if choose_door < 1 or choose_door > how_many_doors:
                      print("¡No existe esa puerta, zopenco! Elige sabiamente")
                      continue
                  else:
                      break
              print(f"\033[34mHas elegido la puerta {choose_door} ¡Suerte en tu porvenir!\033[0m")
              time.sleep(2)

EL juego se desarrollará en un bucle FOR:

          for advance in range(5):
                  time.sleep(0.75)
                  print("", end="", flush=True)
                  clf.doors()
                  clf.event(protagonist)
                    if protagonist.health <= 0:
                      print(f"\n¡Has muerto, {protagonist.name}!")
                      break
    
                    if protagonist.health > 0:
                        final_caption = 'Has logrado escapar de la mazmorra con vida! ¡ENHORABUENA!'
                        for letra in final_caption:
                                print(letra, end="", flush=True)

el evento a ocurrir de entre los 3 desarrollados (descritos mas adelante), se determinará con la siguiente función:

          def event(protagonist):
               event = random.choice(["trap", "combat", "nothing"])
               if event == "trap":
                   trap(protagonist)
               elif event == "combat":
                   combat(protagonist)
               elif event == "nothing":
                   print(quiet_advance(protagonist))

### Eventos:

● Trampa:
Una trampa se activará cuando el jugador avanza y tendrá la posibilidad de esquivarla mediante una mecánica de elección de un número del 1 al 10. Si el numero coincide con el numero que se generará aleatoriamente, logrará esquivar la trampa. Si no, recibirá daño y la aventura continuará. Habrá tambien interacciones con el npc aliado con el que contará el jugador.

          def trap(protagonist):
                    print("\n\033[31m¡Has activado una trampa!\033[0m")
          
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
                    caption8 = "\033[31m¡Prepárate para luchar!\033[0m"
                    for letra in caption8:
                      print(letra, end="", flush=True)
                    time.sleep(0.02)
          
                    while enemy.health > 0 and protagonist.is_alive():
                # Turno del protagonista
                        protagonist_damage = protagonist.attack()
                        enemy.health -= protagonist_damage
                        caption9 = f"\n\033[34mAtacas al {enemy.name} y le haces {protagonist_damage} de daño. Vida del enemigo: {enemy.health}\033[0m\n"
                        for letra in caption9:
                          print(letra, end="", flush=True)
                          time.sleep(0.02)
          
                        if enemy.health <= 0:
                            caption10 = f"\n\033[34m¡Has derrotado al {enemy.name}!\033[0m\n"
                            for letra in caption10:
                              print(letra, end="", flush=True)
                              time.sleep(0.02)
                            return
                # Turno del Enemigo
                        enemy_damage = enemy.Attack()
                        damage_taken = protagonist.take_damage(enemy_damage)
                        caption11 =  f"\033[31mEl {enemy.name} te ataca y te hace {damage_taken} de daño. Tu health: {protagonist.health}\033[0m\n"
                        for letra in caption11:
                              print(letra, end="", flush=True)
                              time.sleep(0.02)
                        time.sleep(1)
          
                    if not protagonist.is_alive():
                        caption12 = f"\n\033[31mEl {enemy.name} te ha derrotado...\033[0m"
                        for letra in caption12:
                              print(letra, end="", flush=True)
                              time.sleep(0.02)


● Cueva/camino tranquilo:
El jugador no encontrará obstáculos. Estos tramos se aprovecharán para dar contexto a la historia y ofrecer descripciones del lugar y dar pie a diaologos con el npc aliado.

          def quiet_advance(protagonist):
     
              path_random = {'path1':"\033[32mContinuas tu camino por la oscura y húmeda mazmorra. La sensación de desamparo te abruma, pero debes seguir adelante.\033[0m", 
              'path2':"\033[33mNo sé como hemos llegado aquí ni por qué, pero algo me dice que esto es obra del destino.\033[0m \033[32m-Dice tu compañero mientras cruzáis el umbral.\033[0m",
              'path3': "\033[32mNotas una ligera brisa de aire desde más adelante. Si la salida está ahí, merecerá la pena continuar sea lo que sea que enfrentes\033[0m",
              'path4': "\033[32mPisas un charco de agua. ¡Agua! Aprovechas y bebes. Tu compañero te mira con recelo. ¿Será potable? Aun así, estás muerto de sed.\033[0m",
              'path5': '\033[32mDetectas rastros de sangre por el suelo y las paredes...\033[0m \033[33m-Se han cometido atrocidades aquí.\033[0m \033[32m-dices entre murmullos-.\033[0m \n'
              '\033[33mVaya ánimos que me traes compañero. Debemos salir de aquí antes de que se percaten de que hemos escapado de la celda.\033[0m'
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

          class Player:
              def __init__(self, name, race):
                  self.name = name
                  self.race = race
                  self.health = chosen_race[race]["health"]
                  self.strength = chosen_race[race]["strength"]
                  self.defence = chosen_race[race]["defence"]
              
              def attack(self):
                      return random.randint(1, self.strength)
          
              def take_damage(self, damage):
                      actual_damage = max(0, damage - self.defence)
                      self.health -= actual_damage
                      return actual_damage
          
              def is_alive(self):
                      return self.health > 0
 
### Enemigos 

Los enemigos se clasificarán en nivel de dificultad fácil, intermedia y difícil:

          class Enemy:
              def __init__(self, name, health, strength):
                  self.name = name
                  self.health = health
                  self.strength = strength
          
              def Attack(self):
                      return random.randint(1, self.strength)
          
              def Appear(self):
                  print(f"\n\033[31m¡Un {self.name} aparece! Vida: {self.health}, Fuerza: {self.strength}\033[0m")
                  time.sleep(2)

● ENEMIGO DIFICULTAD FACIL:

          class Goblin(Enemy):
              def __init__(self):
                  super().__init__("Goblin", health=20, strength=15)

● ENEMIGO DIFICULTAD INTERMEDIA: 

          class Dungeon_boss(Enemy):
              def __init__(self):
                  super().__init__("Guardián de la Mazmorra", health=50, strength=50)

● ENEMIGO DIFICULTAD DIFICIL:

          class GuardianDeLaMazmorra(Enemigo):
              def __init__(self):
                  super().__init__("Guardián de la Mazmorra", vida=50, fuerza=12)
