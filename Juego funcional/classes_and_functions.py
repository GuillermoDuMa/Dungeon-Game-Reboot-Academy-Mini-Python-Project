import time
import random

chosen_race =  {
    "dwarf": {"health": 120, "strength": 8, "defence": 10},
    "elf": {"health": 100, "strength": 10, "defence": 6},
    "human": {"health": 110, "strength": 9, "defence": 8}
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
        print(f"\n¡Un {self.name} aparece! Vida: {self.health}, Fuerza: {self.strength}")


class Goblin(Enemy):
    def __init__(self):
        super().__init__("Goblin", health=20, strength=5)

class Abyss_creature(Enemy):
    def __init__(self):
        super().__init__("The creature of the abyss", health=35, strength=8)

class Dungeon_boss(Enemy):
    def __init__(self):
        super().__init__("Guardián de la Mazmorra", health=50, strength=12)


# FUNCIONES:

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
              enemy_damage = enemy.Attack()
              damage_taken = protagonist.take_damage(enemy_damage)
              print(f"El {enemy.name} te ataca y te hace {damage_taken} de daño. Tu health: {protagonist.health}")
              time.sleep(1)

          if not protagonist.is_alive():
              print(f"\nEl {enemy.name} te ha derrotado...")


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


# Por definir
# def choose_action(): #a medias

#     while True:
#         decision = input ("¿Qué quieres hacer? ¿Avanzar o esperar?")
#         if decision.lower() == "avanzar":
#             print("Avanzas")#llamar funcion para la primera cueva
#             break
#         elif decision.lower() == "esperar":
#             print("Esperando...")
#             time.sleep(1)
#             print("Nada sucede.")
#             time.sleep(1)
#             continue

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

    #return choose_door


        
    

def event(protagonist):
     event = random.choice(["trap", "combat", "nothing"])
     if event == "trap":
         trap(protagonist)
     elif event == "combat":
         combat(protagonist)
     elif event == "nothing":
         print(quiet_advance(protagonist))

