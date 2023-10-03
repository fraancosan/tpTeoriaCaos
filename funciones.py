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


def eleccionTorneo(cromosomas):
  fitness1 = cromosomas[0].valorFitness
  fitness2 = cromosomas[1].valorFitness
  # Si ambos fitness exceden el valor deseado, se elige el menor
  if fitness1 > 1 and fitness2 > 1:
    return min(cromosomas, key=lambda x: x.valorFitness)
  
  # Si ambos fitness son menores al valor deseado, se elige el mayor
  elif fitness1 <= 1 and fitness2 <= 1:
    return max(cromosomas, key=lambda x: x.valorFitness)
  
  # Si uno de los fitness excede el valor deseado, y el otro no hago lo siguiente
  else:
    # Utilizo el valor fitness como numero absoluto
    fitness1 = cromosomas[0].valorFitnessAbs
    fitness2 = cromosomas[1].valorFitnessAbs

    # Elijo el que este mas cerca de la solucion
    if fitness1 < fitness2:
      return cromosomas[0]
    elif fitness1 > fitness2:
      return cromosomas[1]
    
    # En caso de que ambos esten a la misma distancia de la solucion, elijo uno al azar
    else:
      return random.choice(cromosomas)

# Se realiza seleccion por torneo
def torneo(cromosomas):
  seleccionados = []
  for i in range(len(cromosomas)):
    # Se eligen 2 cromosomas al azar
    seleccion = random.sample(cromosomas, 2)
    # Se elige el mejor de los 2
    seleccionados.append(eleccionTorneo(seleccion))
  return seleccionados

def crossover(cromosoma1, cromosoma2, probabilidad, caracteres):
  if random.random() <= probabilidad:
    # Se elige un punto de corte
    puntoCorte = random.choice(range(caracteres))
    # Se realiza el crossover
    valor1 = cromosoma1.valor[:puntoCorte] + cromosoma2.valor[puntoCorte:]
    valor2 = cromosoma2.valor[:puntoCorte] + cromosoma1.valor[puntoCorte:]
    # Se actualizan los cromosomas
    cromosoma1 = cromosoma(caracteres, valor1)
    cromosoma2 = cromosoma(caracteres, valor2)
  return cromosoma1, cromosoma2

def mutacion(cromosoma1, probabilidad, caracteres):
  if random.random() <= probabilidad:
    # Se elige un punto de mutacion
    puntoMutacion = random.choice(range(caracteres))
    valor = cromosoma1.valor
    # Se realiza la mutacion
    if valor[puntoMutacion] == "0":
      valor = valor[:puntoMutacion] + "1" + valor[puntoMutacion+1:]
    else:
      valor = valor[:puntoMutacion] + "0" + valor[puntoMutacion+1:]

    # Se actualiza el cromosoma
    cromosoma1 = cromosoma(caracteres, valor)
  return cromosoma1

def validarIntPos(mensaje):
  while True:
    try:
      cantidad = int(input(mensaje))
      if cantidad <= 0:
        raise ValueError
      break
    except ValueError:
      print("Debe ingresar un numero entero mayor a 0")
  return cantidad

def validarProbabilidad(mensaje):
  while True:
    try:
      cantidad = int(input(mensaje))
      if cantidad <= 0 or cantidad > 100:
        raise ValueError
      break
    except ValueError:
      print("Debe ingresar un porcentaje mayor o igual a 0 y menor o igual a 100")
  return cantidad

class cromosoma:
  def __init__(self, caracteres, valor=None):

    # Si genero el cromosoma sin establecerle un valor, se genera un valor aleatorio
    if valor != None:
      self.valor = valor
    else:
      self.valor = self.generar(caracteres)

    self.entero = self.pasarEntero()
    self.flotante = self.completarNumero()
    self.valorObjetivo = self.objetivo()
    # Mas cerca del 1 es mas cerca de la solucion
    self.valorFitness = self.fitness()

    # Dado que habra resultados mayores a 1, convierto ese fitness en una distancia que me indique que tan lejos esta de la solucion
    # Independientemente de si es mayor o menor a 1
    # Mientras mas cerca a 0, mas cerca de la solucion
    self.valorFitnessAbs = abs(1 - self.valorFitness)

  def limitar(self, nro):
    # Dado que el espacio de solucion es muy grande y se tiene conocimiento de una aproximacion a la solucion, se limita el espacio de solucion
    # Se sabe que el valor se encuentra entre 3 y 4, ademas de que se sabe que el valor flotante es de 6 digitos
    # Por lo tanto se trabajara solo sobre la parte flotante, suponiendo de entrada que el valor sera de 3.algo
    # Devuelve True si hay que regenerar el cromosoma
    nro = int(nro, 2)
    return (0 > nro or nro > 999999)

  def generar(self, caracteres):
    # Se comprueba que la poblacion inicial no se encuentre fuera del espacio de solucion
    # En caso de que se encuentre fuera del espacio de solucion, se regenera el cromosoma
    def comprobar(caracteres):
      valor = crear(caracteres)
      while(self.limitar(valor)):
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
      # Se redondea el resultado a 4 digitos
      return round((tasa*poblacionInicial*(1-poblacionInicial)), 4)

    # Dado que es una funcion recursiva, se fijara un limite de recursividad en 300 años
    # Se toma esa cantidad de años para dar tiempo a que se estabilice la poblacion
    # Dado que la poblacion inicial es irrelevante, se tomara como poblacion inicial 0.4
    valores = [0.4] # Se completa el primer valor, dado que es el valor del primer año
    poblacion = 0.4
    # Se calculan los valores de la poblacion para los proximos 299 años
    for i in range(299):
      poblacion = recursivo(self.flotante, poblacion)
      valores.append(poblacion)
    return valores
  
  def fitness(self):
    # Obtengo como varian los valores de la poblacion a partir del año 70 para dar tiempo a que se llegue a 'estabilizar' la poblacion
    nrosDistintos = len(set(self.valorObjetivo[70:]))

    # Se calcula el fitness, teniendo en cuenta que si hay mas de 32 valores distintos, establecemos que hay caos
    # Mientras mas cerca de 32 valores distintos, mas cerca de la solucion
    fitness = nrosDistintos/32

    return fitness