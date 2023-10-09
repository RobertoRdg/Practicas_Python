canciones = [
    "Canción 1: Letra de la primera canción.",
    "Canción 2: Letra de la segunda canción.",
    "Canción 3: Letra de la tercera canción.",
    "Canción 4: Letra de la cuarta canción.",
    "Canción 5: Letra de la quinta canción.",
    "Canción 6: Letra de la sexta canción.",
    "Canción 7: Letra de la séptima canción.",
    "Canción 8: Letra de la octava canción.",
    "Canción 9: Letra de la novena canción.",
    "Canción 10: Letra de la décima canción."
]

print("Lista de canciones:")
for i, cancion in enumerate(canciones, 1):
    print(f"{i}. {cancion}")

while True:
    try:
        opcion = int(input("Elige un número de canción (1-10): "))
        if 1 <= opcion <= 10:
            break
        else:
            print("Opción no válida. Elige un número entre 1 y 10.")
    except ValueError:
        print("Opción no válida. Elige un número entre 1 y 10.")

cancion_seleccionada = canciones[opcion - 1]
print(f"\nHas elegido:\n{cancion_seleccionada}")