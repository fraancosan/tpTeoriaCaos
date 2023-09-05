import random

# Función de objetivo
def objetivo():
  pass

# Función de fitness
def fitness():
  pass


# Se genera la primer poblacion
def generarPoblacion(tamaño, caracteres):
  poblacion = []
  for i in range(tamaño):
    cromosoma = ""
    for j in range(caracteres):
      cromosoma += str(random.randint(0, 1))
    poblacion.append(cromosoma)
  
  poblacion = comprobarPoblacionInicial(poblacion, caracteres)
  return poblacion
  
# Dado que el espacio de solucion es muy grande y se tiene conocimiento de una aproximacion a la solucion, se limita el espacio de solucion
# Se sabe que el valor se encuentra entre 3 y 4, ademas de que se sabe que el valor flotante es de 6 digitos
# Por lo tanto se trabajara solo sobre la parte flotante, suponiendo de entrada que el valor sera de 3.algo
def limitar(nro):
  nro = int(nro, 2)
  return (0 <= nro and nro <= 999999)

def comprobarPoblacionInicial(poblacion, caracteres):
  for i in range(len(poblacion)):
    while(limitar(poblacion[i])):
      poblacion[i] = generarPoblacion(1, caracteres)[0]

  return poblacion