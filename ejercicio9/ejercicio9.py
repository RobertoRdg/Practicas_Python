total_factura = float(input("Ingresa el total de la factura: $"))

propina_18 = total_factura * 0.18
propina_20 = total_factura * 0.20
propina_25 = total_factura * 0.25

print(f"Para una propina del 18%: ${propina_18:.2f}")
print(f"Para una propina del 20%: ${propina_20:.2f}")
print(f"Para una propina del 25%: ${propina_25:.2f}")

personas = int(input(f"Numero de personas que pagar la cuenta: "))

total18 = (total_factura+propina_18)/personas
total20= (total_factura+propina_20)/personas
total25 = (total_factura+propina_25)/personas

print(f"Dejando una propina del 18% cada persona pagara: ${total18}")
print(f"Dejando una propina del 20% cada persona pagara: ${total20}")
print(f"Dejando una propina del 25% cada persona pagara: ${total25}")