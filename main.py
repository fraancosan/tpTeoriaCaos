from funciones import *
from generadorExcel import generadorExcel

# Se sabe que el valor se encuentra entre 3 y 4, ademas de que se sabe que el valor flotante es de 6 digitos
# Por lo tanto se trabajara solo sobre la parte flotante, suponiendo de entrada que el valor sera de 3.algo

# Cantidad de cromosomas / bits a usar
# Sabiendo que se trabaja con 6 digitos de precision, se necesitan 20 bits para poder representar todos los numeros
caracteres = 20

# Se preguntara y validara la cantidad de individuos por poblacion, solo numeros enteros. Sugerido 50
cantidad = validarIntPos("Ingrese la cantidad de individuos por poblacion - Sugerido 50: ")

# Se preguntara cantidad de ciclos a realizar, solo numeros enteros. Sugerido 300
ciclos = validarIntPos("Ingrese la cantidad de ciclos a realizar - Sugerido 300: ")

# Se preguntara y validara la probabilidad de mutacion, solo numeros enteros entre 0 y 100. Sugerido 10
probabilidadMutacion = validarProbabilidad("Ingrese la probabilidad de mutacion a utilizar, entre 0 y 100- Sugerido 10: ")

# Se preguntara y validara la probabilidad de cruce, solo numeros enteros entre 0 y 100. Sugerido 75
probabilidadCruce = validarProbabilidad("Ingrese la probabilidad de cruce a utilizar, entre 0 y 100 - Sugerido 75: ")

print(f"\nSe trabajara con una poblacion de {cantidad} individuos, {caracteres} genes por individuo y {ciclos} ciclos de ejecucion")
print(f"Se utilizara una probabilidad de mutacion de {probabilidadMutacion}% y una probabilidad de cruce de {probabilidadCruce}%")

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
            poblacion.extend(crossover(seleccionados[i], seleccionados[i+1], probabilidadCruce, caracteres))

        # Mutacion
        for i in range(cantidad):
            poblacion[i] = mutacion(poblacion[i], probabilidadMutacion, caracteres)
    
    # Guardo el mejor resultado de cada ejecucion
    mejoresResultados.append(min(poblacion, key=lambda x: x.valorFitnessAbs))

excel = generadorExcel()
excel.generar(mejoresResultados, ciclos, caracteres, cantidad, probabilidadMutacion, probabilidadCruce)