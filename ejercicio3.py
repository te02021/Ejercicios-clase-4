"""
Escribir un programa que pida al usuario un número entero positivo y 
muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.
"""


def impar(num):
    lista = []
    for i in range(1, num + 1, 2):
        lista.append(str(i))
    resultado = ", ".join(lista)
    return resultado

numero = int(input("Ingrese un numero entero positivo: "))

mi_resultado = impar(numero)

print(f"Los numeros impares desde 1 hasta {numero} son: {mi_resultado}")
    
