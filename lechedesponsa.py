precio_por_unidad = 1000
cantidad = int(input("Ingrese la cantidad de unidades de leche compradas: "))
es_jubilado = input("¿Es usted jubilado? (sí/no): ")
descuento = 0
if cantidad > 24:
    descuento = 0.15
elif cantidad > 12:
    descuento = 0.10
if es_jubilado == 'sí':
    descuento += 0.10
costo_total = cantidad * precio_por_unidad * (1 - descuento)

print(f"El costo total a pagar es: {costo_total:.2f} pesos")