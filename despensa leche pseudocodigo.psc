
	Algoritmo calcularCostoTotal
		Definir precio_por_unidad Como Real
		Definir cantidad Como Entero
		Definir es_jubilado Como Cadena
		Definir descuento Como Real
		Definir costo_total Como Real
		
		precio_por_unidad <- 1000
		Escribir "Ingrese la cantidad de unidades de leche compradas: "
		Leer cantidad
		Escribir "¿Es usted jubilado? (sí/no): "
		Leer es_jubilado
		
		descuento <- 0
		
		Si cantidad > 24 Entonces
			descuento <- 0.15
		Sino
			Si cantidad > 12 Entonces
				descuento <- 0.10
			FinSi
		FinSi
		
		Si es_jubilado = "sí" Entonces
			descuento <- descuento + 0.10
		FinSi
		
		costo_total <- cantidad * precio_por_unidad * (1 - descuento)
		
		Escribir "El costo total a pagar es: ", costo_total, " pesos"
FinAlgoritmo
