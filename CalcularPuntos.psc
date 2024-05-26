Algoritmo CalcularPuntos
    Definir ganados Como Entero
    Definir empatados Como Entero
    Definir perdidos Como Entero
    Definir puntos Como Entero
	
    Escribir "Ingrese la cantidad de partidos ganados: "
    Leer ganados
	
    Escribir "Ingrese la cantidad de partidos empatados: "
    Leer empatados
	
    Escribir "Ingrese la cantidad de partidos perdidos: "
    Leer perdidos
	
    puntos = (ganados * 3) + (empatados * 1) + (perdidos * 0)
	
    Escribir "La cantidad de puntos acumulados por el equipo es: ", puntos
FinAlgoritmo
