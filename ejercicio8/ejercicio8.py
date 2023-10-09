palabras = []
for i in range(5):
    palabra = input(f"Ingresa la palabra #{i+1}: ")
    palabras.append(palabra)

def es_palindromo(palabra):
    palabra = palabra.lower()
    return palabra == palabra[::-1]

palindromos = [palabra for palabra in palabras if es_palindromo(palabra)]

if palindromos:
    print("Las siguientes palabras son palíndromos:")
    for palindromo in palindromos:
        print(palindromo)
else:
    print("Ninguna de las palabras ingresadas es un palíndromo.")