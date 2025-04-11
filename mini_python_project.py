import random
import time

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


race = {
    "enano": {"vida": 120, "fuerza": 8, "defensa": 10},
    "elfo": {"vida": 100, "fuerza": 10, "defensa": 6},
    "hombre": {"vida": 110, "fuerza": 9, "defensa": 8}

}

# Crea una clase para el jugador
class Jugador:  
    def __init__(self, raza):
        self.raza = raza
        self.vida = race[raza]["vida"]
        self.fuerza = race[raza]["fuerza"]
        self.defensa = race[raza]["defensa"]

def choose_action(): #a medias
    while True:
        decision = input ("¿Qué quieres hacer? ¿Avanzar o esperar?")
        if decision.lower() == "avanzar":
            print("a medias")#llamar funcion para la primera cueva
        elif decision.lower() == "esperar":
            print("Esperando...")
            time.sleep(1)
            print("Nada sucede.")
            time.sleep(1)
            continue
#funcion combate        
def combate(jugador):
    enemigo_fuerza = random.randint(5, 12)
    print(f"¡Un enemigo aparece con fuerza {enemigo_fuerza}!")
    daño = max(0, enemigo_fuerza - jugador.defensa)
    jugador.vida -= daño
    print(f"Has recibido {daño} de daño. Vida restante: {jugador.vida}")
#funcion seleccionar raza
def select_raza():

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

# Define las razas y estadísticas
name= input("¿Cómo deberían llamarte?: ")
time.sleep(1)
print("¡Un gran nombre!")
time.sleep(2)
print("¡Bien! Vamos allá...")
time.sleep(1)
    
select_raza()    



caption_intro1 = """\033[32mNotas una helada brisa en la nuca, arrugas los ojos y parpadeas con esfuerzo. Te levantas, la cabeza te da vueltas como si te hubieran golpeado.
Luchas por ver frente a ti, esta oscuro; increiblemente oscuro. Consigues ver algo cerca tuya. ¿Que es...?\033[0m
\033[33mPor fin despiertas\033[0m \033[32m---Escuchas y meneas la cabeza.\033[0m
\033[33m¿Donde estoy?\033[0m \033[32m--susurras. \033[0m
\033[33mEstamos atrapados. \033[0m \033[32m--dice la silueta. No reconoces... esa voz.\033[0m"""
for letra in caption_intro1:
    print(letra, end="", flush=True)
    time.sleep(0.02)
choose_action()

    


# 4. Mecánicas del juego (avances y eventos)


# trampas

# Puedes hacer algo muy simple al principio, como restar vida con base en fuerza o probabilidad.



def trampa(jugador):
    daño = random.randint(5, 15)
    jugador.vida -= daño
    print(f"¡Has caído en una trampa! Pierdes {daño} de vida. Vida restante: {jugador.vida}")

# ✅ 6. Ciclo principal del juego




# ✅ 7. Ejecutar el juego


