"""
Escribir un programa que muestre el eco de todo lo que el usuario introduzca
hasta que el usuario escriba “salir” que terminará.
"""


while True:
    texto = input("Ingrese su texto: ")
    texto_m = texto.lower()
    if texto_m == "salir":
        break
    print(texto_m)
