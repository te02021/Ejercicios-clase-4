"""
Escribir un programa que pida al usuario un número entero y 
muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.
"""




    
def t_r(numero):
    #codigo
    mi_dic = {}
    for i in range(1, numero + 1):
        mi_dic[i] = "*"*i
    resultado = "\n".join(mi_dic.values())
    return resultado
    
numero = int(input("Ingrese el numero: "))



print(t_r(numero))