"""
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, 
y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.
"""

cantidad_invertir = float(input("Ingrese la cantidad a invertir: "))
interes_anual = float(input("Ingrese el interés anual en porcentaje: "))
anios = int(input("Ingrese los años: "))

for anio in range(1, anios + 1):
    capital = cantidad_invertir * (1 + interes_anual / 100) ** anio
    print(f"Año: {anio}, Capital: {capital}")

