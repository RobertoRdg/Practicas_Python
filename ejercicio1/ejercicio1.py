while True:
    try:
        numero = int(input("Ingresa un número entre 1 y 1000: "))
        if 1 <= numero <= 1000:
            if numero % 2 == 0:
                print(f"El número {numero} es par.")
            else:
                print(f"El número {numero} es impar.")
                break
        else:
            print("Opción no válida. Debes elegir un número entre 1 y 1000.")
    except ValueError:
        print("Opción no válida. Debes elegir un número entre 1 y 1000.")