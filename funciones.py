import random

# Se obtienen los valores objetivos de cada individuo
def objetivoPoblacional(cromosomas):
  valores = []
  for cromosoma in cromosomas:
    valores.append(cromosoma.valorObjetivo)
  return valores


# Se obtiene el fitness de cada individuo
def fitnessPoblacional(cromosomas):
  valoresFitness = []
  for cromosoma in cromosomas:
    valoresFitness.append(cromosoma.valorFitness)
  return valoresFitness

# Se genera la poblacion inicial
def generarPoblacionInicial(tamaño, caracteres):
  poblacion = []
  for i in range(tamaño):
    poblacion.append(cromosoma(caracteres))

  return poblacion

class cromosoma:
  def __init__(self, caracteres):
    self.valor = self.generar(caracteres)
    self.entero = self.pasarEntero()
    self.flotante = self.completarNumero()
    self.valorObjetivo = self.objetivo()
    self.valorFitness = self.fitness()

  def generar(self, caracteres):
    def limitar(nro):
      # Dado que el espacio de solucion es muy grande y se tiene conocimiento de una aproximacion a la solucion, se limita el espacio de solucion
      # Se sabe que el valor se encuentra entre 3 y 4, ademas de que se sabe que el valor flotante es de 6 digitos
      # Por lo tanto se trabajara solo sobre la parte flotante, suponiendo de entrada que el valor sera de 3.algo
      # Devuelve True si hay que regenerar el cromosoma
      nro = int(nro, 2)
      return (0 > nro or nro > 999999)
    
    # Se comprueba que la poblacion inicial no se encuentre fuera del espacio de solucion
    # En caso de que se encuentre fuera del espacio de solucion, se regenera el cromosoma
    def comprobar(caracteres):
      valor = crear(caracteres)
      while(limitar(valor)):
        valor = crear(caracteres)
      return valor

    def crear(caracteres):
      cromosoma = ""
      for i in range(caracteres):
        cromosoma += str(random.randint(0, 1))
      return cromosoma
    
    # Se genera el cromosoma y se comprueba que se encuentre dentro del espacio de solucion
    return comprobar(caracteres)

  def pasarEntero(self):
    return int(self.valor, 2)
  
  def completarNumero(self):
    return float("3." + str(self.pasarEntero()))

  def objetivo(self):
    def recursivo(tasa, poblacionInicial):
      # Se redondea el resultado a 6 digitos
      return round((tasa*poblacionInicial*(1-poblacionInicial)), 6)

    # Dado que es una funcion recursiva, se fijara un limite de recursividad en 300 años
    # Se toma esa cantidad de años para dar tiempo a que se estabilice la poblacion
    # Dado que la poblacion inicial es irrelevante, se tomara como poblacion inicial 0.4
    # Se completa el primer valor, dado que es el valor del primer año
    valores = [0.4]
    poblacion = 0.4
    # Se calculan los valores de la poblacion para los proximos 299 años
    for i in range(299):
      poblacion = recursivo(self.flotante, poblacion)
      valores.append(poblacion)
    return valores
  
  # Función de fitness en cuanto a la cercania al limite de caos
  def fitness(self):
    # Obtengo como varian los valores de la poblacion a partir del año 70 para dar tiempo a que se llegue a estabilizar la poblacion
    nrosDistintos = len(set(self.valorObjetivo[70:]))

    # Se calcula el fitness, teniendo en cuenta que si hay mas de 64 valores distintos, establecemos que hay caos
    # Mientras mas cerca de 64 valores distintos, mas cerca de la solucion
    fitness = nrosDistintos/64

    # Dado que habra resultados mayores a 1, convierto ese fitness en una distancia que me indique que tan lejos esta de la solucion
    # Independientemente de si es mayor o menor a 1
    # Mientras mas cerca a 0, mas cerca de la solucion
    return abs(1 - fitness)

  def actualizar(self, valor):
    self.valor = valor
    self.entero = self.pasarEntero()
    self.flotante = self.completarNumero()
    self.valorObjetivo = self.objetivo()
    self.fitness = self.fitness()