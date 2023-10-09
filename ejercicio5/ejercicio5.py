significado_completo = input("Escribe el significado completo de una organización o concepto: ")

palabras = significado_completo.split()

acronimo = "".join([palabra[0].upper() for palabra in palabras])

print(f"El acrónimo para '{significado_completo}' es '{acronimo}'.")