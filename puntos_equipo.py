"""Un hincha de fútbol desea conocer la cantidad de puntos que su
equipo lleva acumulados en el campeonato, para ello recibe cada semana la
información de la cantidad total de partidos, desde el inicio del campeonato, que
el equipo ha perdido, ha empatado y ha ganado. Por cada partido empatado
recibe un punto, por cada partido ganado tres puntos y por los perdidos cero
puntos."""

cant_part_gan = int(input ("Bienvenido! Por favor ingrese la cantidad de partidos ganados durante el campeonato: "))

cant_part_emp = int(input ("Perfecto! Ahora por favor ingrese la cantidad de partidos empatados: "))

cant_part_per = int(input ("Por ultimo, ingrese la cantidad de partidos perdidos: "))

punt_gan = cant_part_gan * 3
print(punt_gan)
punt_emp = cant_part_emp * 1
print(punt_emp)
punt_per = cant_part_per * 0
print(punt_per)
total_puntos = punt_emp + punt_gan + punt_per

print (" El equipo acumuló un total de ", total_puntos, "en lo que va del campeonato")