import random

# Función objetivo
def objetivo(tasa, poblacion):
  return (tasa*poblacion*(1-poblacion))

def realizarObjetivo(tasa):
  # Dado que es una funcion recursiva, se fijara un limite de recursividad en 200 años
  # Se toma esa cantidad de años para dar tiempo a que se estabilice la poblacion
  # Dado que la poblacion inicial es irrelevante, se tomara como poblacion inicial 0.4
  # Se completa el primer valor, dado que es el valor del primer año
  valores = [0.4]
  poblacion = 0.4
  # Se calculan los valores de la poblacion para los proximos 199 años
  for i in range(199):
    poblacion = objetivo(tasa, poblacion)
    valores.append(poblacion)
  return valores

# Se realiza la funcion objetivo por cada individuo de la poblacion
def realizarObjetivoLista(tasas):
  valores = []
  for tasa in tasas:
    valores.append(realizarObjetivo(tasa))
  return valores

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
# Devuelve True si hay que regenerar el cromosoma
def limitar(nro):
  nro = int(nro, 2)
  return (0 > nro or nro > 999999)

def comprobarPoblacionInicial(poblacion, caracteres):
  for i in range(len(poblacion)):
    while(limitar(poblacion[i])):
      poblacion[i] = generarPoblacion(1, caracteres)[0]

  return poblacion



# Funciones para pasar de binario a decimal
def pasarEntero(lista):
  numeros = []
  for numero in lista:
    numeros.append(int(numero, 2))
  return numeros

def completarNumeros(lista):
  numeros = []
  lista = pasarEntero(lista)
  # se añade a cada numero el valor 3, dejando el resto del numero como decimal
  for numero in lista:
    numeros.append(float("3." + str(numero)))
  return numeros