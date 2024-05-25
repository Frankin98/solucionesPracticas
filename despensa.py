"""Una despensa de barrio vende la leche de vaca entera de litro a 1000 pesos la unidad. 
Si el cliente compra más de 12  unidades (y hasta 24 unidades), el costo tiene un descuento del 10%. 
Si compra más de 24 unidades, el descuento es del 15%. Además posee la promoción a los jubilados. 
La promoción de jubilados es sumarle un 10% de descuento (si posee otros descuentos, se suma los descuentos). 
Desarrolle una solución algorítmica para saber cuento debe pagar el cliente."""

leche = 1000

"""descuento por cantidad 12/24"""
desc_cant = 0.10 

"""descuento por +24"""
desc_cant_a = 0.15

"""descuento jubilado"""
desc_jub = 0.10

"""descuento por cantidad 12/24 + jubilado"""
desc_subtotal = desc_cant + desc_jub

"""descuento por más 24 leches + jubilado"""
desc_total = desc_cant_a + desc_jub

canti_compra = int(input("Hola buen dia! ¿Cuantas leches desea llevar el cliente? " ))

subtotal = canti_compra * leche

jubi = int(input("¿El cliente es jubilado? Si lo es escriba 0, caso contrario escriba 1: "))

if canti_compra >= 12 and canti_compra <= 24 and jubi == 0 :
    total = subtotal - (subtotal * desc_subtotal)
    print ("El total a abonar sin descuento es $", subtotal," por el descuento de cantidad y jubilado es: $", total)

elif canti_compra >= 12 and canti_compra <= 24 and jubi == 1:
    total = subtotal - (subtotal * desc_cant)
    print ("El total a abonar sin descuento es: $", subtotal, " por el descuento de cantidad es: $", total)

elif canti_compra > 24 and jubi == 0:
    total = subtotal - (subtotal * desc_total)
    print ("El total a abonar sin descuento es: $", subtotal, " por el descuento de cantidad y jubilado es: $", total)

elif canti_compra > 24 and jubi == 1:
    total = subtotal - (subtotal * desc_cant_a)
    print ("El total a abonar sin descuento es: $", subtotal, " por el descuento de cantidad es: $", total)

elif canti_compra < 12 and jubi == 0:
    total = subtotal - (subtotal * desc_jub)
    print ("El total a abonar sin descuento es: $", subtotal, " por el descuento de jubilado es: $", total)

elif canti_compra < 12 and jubi == 1:
    print("El total a abonar es: $", subtotal)
