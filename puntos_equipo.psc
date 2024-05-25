Algoritmo puntos_equipo
	Escribir "Bienvenido! Por favor ingrese la cantidad de partidos ganados durante el campeonato: "
	leer cant_part_gan
	Escribir "Perfecto! Ahora por favor ingrese la cantidad de partidos empatados: "
	leer cant_part_emp
	Escribir "Por ultimo, ingrese la cantidad de partidos perdidos: "
	Leer cant_part_per
	puntos_ganados = cant_part_gan * 3
	puntos_empate = cant_part_emp * 1
	puntos_perdida = cant_part_per * 0
	total_puntos = puntos_ganados + puntos_empate + puntos_perdida
	Mostrar "Su equipo tiene un total de ", total_puntos, " en el torneo"
FinAlgoritmo
