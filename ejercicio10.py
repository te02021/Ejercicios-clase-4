"""
Escribir un programa que pida al usuario un número entero y 
muestre por pantalla si es un número primo o no.
"""

numero = int(input("Ingrese un numero entero: "))

if numero<2:
    primo = False
else:
    primo = True
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            primo == False
            break

if primo:
    print(f"{numero} es primo")
else:
    print(f"{numero} no es primo")
            
    