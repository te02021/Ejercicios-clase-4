"""
Escribir un programa que pida al usuario un número entero positivo y 
muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.
"""

numero = int(input("Ingrese el numero entero positivo: "))

for i in range(0, numero+1):
    print(numero, end=", ")
    numero -= 1