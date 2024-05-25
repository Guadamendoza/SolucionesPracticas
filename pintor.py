ancho = float(input("Ingrese el ancho de la pared en metros: "))
alto = float(input("Ingrese el alto de la pared en metros: "))
costo_por_metro_cuadrado = float(input("Ingrese el costo de mano de obra por metro cuadrado: "))
area= ancho* alto
costo_total = area* costo_por_metro_cuadrado
print (f"El costo de mano de obra para pintar la pared es: {costo_total:.2f}")
