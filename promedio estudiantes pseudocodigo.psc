
	Algoritmo promedioestudiantes
		Definir cantidad_estudiantes Como Entero
		Definir suma_notas Como Real
		Definir nota Como Real
		Definir promedio Como Real
		Definir rendimiento Como Caracter
		suma_notas = 0
		Escribir "Ingrese la cantidad de estudiantes que han rendido el examen: "
		Leer cantidad_estudiantes
		Para i = 1 Hasta cantidad_estudiantes Hacer
			Escribir "Ingrese la nota del estudiante ", i, ": "
			Leer nota
			suma_notas = suma_notas + nota
		FinPara
		promedio = suma_notas / cantidad_estudiantes
		
		Si promedio > 8 Entonces
			rendimiento = "elevado"
		Sino
			Si promedio >= 6 Entonces
				rendimiento = "aceptable"
			Sino
			rendimiento = "bajo"
			FinSi
		FinSi
		Escribir "El promedio de notas es: ", promedio
		Escribir "El rendimiento del curso es: ", rendimiento
FinAlgoritmo
