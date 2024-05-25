"""Un pintor de casas debe hacer un presupuesto para un cliente. Lo que cobra se calcula de acuerdo a los 
metros cuadrados que debe pintar. El cliente le indica que necesita conocer el costo de mano de obra para 
pintar una pared rectangular de un galpón. El pintor cobra un monto ﬁjo por cada metro cuadrado. 
Puedes hacer un algoritmo para calcular el costo de mano de obra para pintar la pared."""

cost_mc = 100

cant_mc = float(input("Buenos días, para obtener un presupuesto por favor indique en números la cantida de metros cuadrados de lo que desea pintar: "))

presu = cost_mc * cant_mc

print ("El presupuesto es de: $", presu)

