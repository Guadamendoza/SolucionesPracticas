cantidad_estudiantes = int(input("Ingrese la cantidad de estudiantes que han rendido el examen: "))
suma_notas = 0
for i in range(cantidad_estudiantes):
    nota = float(input(f"Ingrese la nota del estudiante {i + 1}: "))
    suma_notas += nota
promedio = suma_notas / cantidad_estudiantes
if promedio > 8:
    rendimiento = "elevado"
elif 6 <= promedio <= 8:
    rendimiento = "aceptable"
else:
    rendimiento = "bajo"
print(f"El promedio de notas es: {promedio:.2f}")
print(f"El rendimiento del curso es: {rendimiento}")