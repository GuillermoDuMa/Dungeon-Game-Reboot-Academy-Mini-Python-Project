import time
import random
import classes_and_functions as clf
from classes_and_functions import Player

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

name = input("What is your name, warrior?: ")
time.sleep(1)
print("¡Un gran nombre!")
time.sleep(2)
print("¡Bien! Vamos allá...")
time.sleep(1)
race = input("¿Cual es tu raza?: dwarf, elf, human): ").lower()
protagonist = Player(name, race)
print(f"{protagonist.name} el {protagonist.race.capitalize()} tiene {protagonist.health} de health.")

caption_intro1 = """\033[32mNotas una helada brisa en la nuca, arrugas los ojos y parpadeas con esfuerzo. Te levantas, la cabeza te da vueltas como si te hubieran golpeado.
Luchas por ver frente a ti, esta oscuro; increiblemente oscuro. Consigues ver algo cerca tuya. ¿Que es...?\033[0m
\033[33mPor fin despiertas\033[0m \033[32m---Escuchas y meneas la cabeza.\033[0m
\033[33m¿Donde estoy?\033[0m \033[32m--susurras. \033[0m
\033[33mEstamos atrapados. \033[0m \033[32m--dice la silueta. No reconoces... esa voz.\033[0m"""
for word in caption_intro1:
    print(word, end="", flush=True)
    time.sleep(0.02)




#### FOR

print("añadir intro aqui mpare")

print(" añadir dialogo para elegir camino")

for advance in range(5):
        time.sleep(0.75)
        print(".", end="", flush=True)
        clf.doors()
        clf.event(protagonist)
        if protagonist.health <= 0:
            print(f"\n¡Has muerto, {protagonist.name}!")
            break
print("has logrado escapar de la mazmorra con vida! ¡VICTORIA!") 

