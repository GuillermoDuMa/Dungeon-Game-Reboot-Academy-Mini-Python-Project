import time
import random

chosen_race =  {
    "dwarf": {"health": 125, "strength": 10, "defence": 9},
    "elf": {"health": 90, "strength": 20, "defence": 6},
    "human": {"health": 110, "strength": 15, "defence": 8}
        }

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


class Goblin(Enemy):
    def __init__(self):
        super().__init__("Goblin", health=20, strength=15)

class Bloody_Unicorn(Enemy):
    def __init__(self):
        super().__init__("Bloody Unicorn", health=40, strength=20)

class Abyss_creature(Enemy):
    def __init__(self):
        super().__init__("The creature of the abyss", health=35, strength=25)

class Dungeon_boss(Enemy):
    def __init__(self):
        super().__init__("Guardián de la Mazmorra", health=50, strength=35)


# FUNCIONES:

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

def combat(protagonist):
          possible_enemies = [Goblin(), Abyss_creature(), Dungeon_boss(), Bloody_Unicorn()]
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


def choose_action(protagonist):
    espera_count = 0  # mantener el nombre consistente
    while True:
        decision = input("\033[34m¿Qué quieres hacer? ¿Avanzar o esperar?: \033[0m")
        if decision.lower() == "avanzar":
            print("Avanzas")  # aquí iría tu lógica de avanzar
            break
        elif decision.lower() == "esperar":
            espera_count += 1
            print("Esperando...")
            time.sleep(1)
            print("Sigues esperando...")
            time.sleep(2)
            if espera_count >= 5:
                print("\033[31mEstá bien, tú lo has querido: ¡Los monstruos aparecen!\033[0m")
                time.sleep(1)
                combat(protagonist)
                continue
            elif espera_count >= 3 and espera_count <= 3:
                print("\033[31m¿De verdad piensas seguir esperando?\033[0m")
                time.sleep(1)
        else:
            print("Elige bien (escribe 'avanzar' o 'esperar').")
     

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

    #return choose_door


        
    

def event(protagonist):
     event = random.choice(["trap", "combat", "nothing"])
     if event == "trap":
         trap(protagonist)
     elif event == "combat":
         combat(protagonist)
     elif event == "nothing":
         print(quiet_advance(protagonist))

