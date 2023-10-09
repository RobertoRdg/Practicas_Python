import random

numero_secreto = random.randint(1, 50)

intentos = 0

while True:
    intento = input("Adivina un número entre 1 y 50: ")

    if intento.lower() == 'salir':
        print(f"El número secreto era {numero_secreto}. ¡Hasta luego!")
        break

    if not intento.isdigit() or int(intento) < 1 or int(intento) > 50:
        print("Ingresa un número válido dentro del rango de 1 a 50.")
        continue

    intento = int(intento)

    intentos += 1

    if intento == numero_secreto:
        print(f"¡Felicitaciones! Adivinaste el número secreto ({numero_secreto}) en {intentos} intentos.")
        break
    elif intento < numero_secreto:
        print("El número secreto es mayor. Inténtalo nuevamente.")
    else:
        print("El número secreto es menor. Inténtalo nuevamente.")