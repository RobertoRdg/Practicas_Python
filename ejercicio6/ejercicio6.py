import random

opciones = ["piedra", "papel", "tijera"]

usuario = input("Elige piedra, papel o tijera: ").lower()

computadora = random.choice(opciones)

print(f"Usuario eligió: {usuario}")
print(f"Computadora eligió: {computadora}")

if usuario == computadora:
    print("¡Empate!")
elif usuario == "piedra" and computadora == "tijera" or usuario == "papel" and computadora == "piedra" or usuario == "tijera" and computadora == "papel":
    print("¡Ganaste!")
else:
    print("¡La computadora gana!")
