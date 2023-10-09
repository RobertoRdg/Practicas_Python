correo_electronico = input("Ingresa tu dirección de correo electrónico: ")

nombre_usuario, dominio = correo_electronico.split('@', 1)

nombres_de_dominio_populares = ["gmail.com", "yahoo.com", "outlook.com", "hotmail.com"]

if dominio.lower() in nombres_de_dominio_populares:
    print(f"Tu dirección de correo electrónico '{correo_electronico}' tiene un nombre de dominio popular.")
else:
    print(f"Tu dirección de correo electrónico '{correo_electronico}' tiene un nombre de dominio personalizado.")