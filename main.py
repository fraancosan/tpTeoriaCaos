from openpyxl import Workbook
from openpyxl.styles import Border, Side, Font, Alignment
import random
import os
from statistics import mean
import matplotlib.pyplot as plt
from bitstring import BitArray

# El resultado a obtener deberia ser 3.759816

caracteres = 64
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
