from openpyxl import Workbook
from openpyxl.styles import Border, Side, Font, Alignment
import random
import os
from statistics import mean
import matplotlib.pyplot as plt
from funciones import *

# El resultado a obtener deberia ser 3.759816
# Se sabe que el valor se encuentra entre 3 y 4, ademas de que se sabe que el valor flotante es de 6 digitos
# Por lo tanto se trabajara solo sobre la parte flotante, suponiendo de entrada que el valor sera de 3.algo

# Cantidad de individuos por poblacion
cantidad = 10

# Cantidad de cromosomas / bits a usar
# Sabiendo que se trabaja con 6 digitos de precision, se necesitan 20 bits para poder representar todos los numeros
caracteres = 20

# Cantidad de ciclos a realizar
ciclos = 200

#Verificamos si se usa metodo de ruleta o torneo

ruleta = input("Desea utilizar el metodo de ruleta o torneo (r/t): ")
while (ruleta != "r" and ruleta != "t"):
    ruleta = input("Desea utilizar el metodo de ruleta o torneo (r/t): ")
if (ruleta == "r"):
    #Si se usa metodo ruleta, vemos si se usa elitismo
    ruleta = True
    utilizaElitismo = input("Desea utilizar elitismo (s/n): ")
    while (utilizaElitismo != "s" and utilizaElitismo != "n"):
        utilizaElitismo = input("Desea utilizar elitismo (s/n): ")

    if (utilizaElitismo == "s"):
        utilizaElitismo = True
    else:
        utilizaElitismo = False
else:
    ruleta = False
    utilizaElitismo = False


# Ejecucion del algoritmo genetico
poblacion = generarPoblacion(cantidad, caracteres)
