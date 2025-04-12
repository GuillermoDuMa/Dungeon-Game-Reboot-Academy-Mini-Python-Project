# Dungeon-Game-Reboot-Academy-Mini-Python-Project

## Escape de la Mazmorra

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

● Combate: 
El jugador se topará con un enemigo al que tendrá que batir para poder continuar. Diversidad de enemigos:

● Cueva/camino tranquilo:
El jugador no encontrará obstáculos. Estos tramos se aprovecharán para dar contexto a la historia y ofrecer descripciones del lugar y dar pie a diaologos con el npc aliado.

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


    def combate(atacar, bloquear):
    
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






