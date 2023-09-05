from bitstring import BitArray

# Función de objetivo
def objetivo():
  pass

# Función de fitness
def fitness():
  pass


# Conversiones de Numeros
# Se hace de esta manera dado que las funciones de python no son tan precisas

# Convertir numero real a Binario
def binario(nro):
  return BitArray(float=nro, length=64).bin

# Convertir numero binario a real
def real(nro):
  return BitArray(bin=nro).float