from funciones import *
from generadorExcel import generadorExcel

# Se sabe que el valor se encuentra entre 3 y 4, ademas de que se sabe que el valor flotante es de 6 digitos
# Por lo tanto se trabajara solo sobre la parte flotante, suponiendo de entrada que el valor sera de 3.algo

# Cantidad de individuos por poblacion
cantidad = 100

# Cantidad de cromosomas / bits a usar
# Sabiendo que se trabaja con 6 digitos de precision, se necesitan 20 bits para poder representar todos los numeros
caracteres = 20

# Cantidad de ciclos a realizar
ciclos = 300


print("Se trabajara con una poblacion de", cantidad, "individuos,", caracteres, "cromosomas y", ciclos, "ciclos")

# Dado que los valores a encontrar varian, se ejecuta el programa 10 veces con distintas poblaciones iniciales para obtener mejores resultados
mejoresResultados = []
for i in range(10):
    # Ejecucion del algoritmo genetico
    poblacion = generarPoblacionInicial(cantidad, caracteres)

    # Se producen los ciclos
    for ciclo in range(1, ciclos+1):
        # Se obtienen los valores objetivos de cada individuo
        valoresObjetivos = objetivoPoblacional(poblacion)

        # Se obtienen los fitness de cada individuo
        valoresFitness = fitnessPoblacional(poblacion)

        # Obtengo candidatos a realizar operaciones de cruce y mutacion
        seleccionados = torneo(poblacion)        
        poblacion = []

        # Crossover
        for i in range(0, cantidad, 2):
            # Solo sucede si las probabilidades se cumplen
            poblacion.extend(crossover(seleccionados[i], seleccionados[i+1], 0.75, caracteres))

        # Mutacion
        for i in range(cantidad):
            poblacion[i] = mutacion(poblacion[i], 0.1, caracteres)
    
    # Guardo el mejor resultado de cada ejecucion
    mejoresResultados.append(min(poblacion, key=lambda x: x.valorFitnessAbs))

excel = generadorExcel()
excel.generar(mejoresResultados)