for numeroEntero in range(0,151):
	print(numeroEntero)

for multiplosdeCinco in range(5,1001,5):
    print(multiplosdeCinco)

"""Contar, a la manera del Dojo: imprime números enteros del 1 al 100. Si es divisible por 5, imprime "Coding” en su lugar.
 Si es divisible por 10, imprime "Coding Dojo"."""

for multiplosdeCinco in range(5,1001):
	if multiplosdeCinco%5==0:
		print(multiplosdeCinco, "Sí, es multiplo")
	else:
		print(multiplosdeCinco, "No, es multiplo")

"""for contarDojo in range(1,101)
	if contarDojo %5==0
		print(contarDojo)"""

"""Contador flexible: establece tres variables: 
lowNum, highNum, mult. Comenzando en lowNum y pasando por highNum, 
imprime solo los enteros que sean múltiplos de mult. 
Por ejemplo, si lowNum=2, highNum=9 y mult=3. El bucle debe imprimir 3, 6, 9 (en líneas sucesivas)"""

highNumber = 9
lowNumber = 2
mult = 3
for contadorFlexible in range(lowNumber, highNumber+1):
	if %mult == 0:
            print(contadorFlexible) 

for contarDojo in range(1,101):
    if i%10==0:
        print("Coding Dojo")
    elif i%5==0:
        print("Coding")
    else:
        print(contarDojo)

# Whoa. Es un gran idiota
suma = 0
for i in range(0,500001):
    if i%2==1:
        suma += i
print(suma)

#Cuenta regresiva por 4
# For Loop 2018 to 0, decrement by 4
for cuentaRegresiva in range(2018,0,-4):
    print(cuentaRegresiva)
