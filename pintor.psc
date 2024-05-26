Algoritmo CalcularCostoManoDeObra
    Definir ancho Como Real
    Definir alto Como Real
    Definir costo_por_metro_cuadrado Como Real
    Definir area Como Real
    Definir costo_total Como Real
	
    Escribir "Ingrese el ancho de la pared en metros: "
    Leer ancho
	
    Escribir "Ingrese el alto de la pared en metros: "
    Leer alto
	
    Escribir "Ingrese el costo de mano de obra por metro cuadrado: "
    Leer costo_por_metro_cuadrado
	
    area = ancho * alto
    costo_total = area * costo_por_metro_cuadrado
	
    Escribir "El costo de mano de obra para pintar la pared es: ", costo_total
FinAlgoritmo

