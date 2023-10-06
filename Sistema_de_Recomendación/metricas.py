import numpy as np

def pearson(r1, r2):
  # Calcula la correlación de Pearson
  correlation = np.corrcoef(r1, r2)[0, 1]

  print(f"La correlación de Pearson entre los dos conjuntos de datos es: {correlation}")

def cosinedistance(r1, r2):
  # Calcular el producto escalar de los vectores
  producto_escalar = np.dot(r1, r2)

  # Calcular las normas de los vectores
  norma_a = np.linalg.norm(r1)
  norma_b = np.linalg.norm(r2)

  # Calcular la distancia del coseno
  distancia_coseno = producto_escalar / (norma_a * norma_b)

  print("Distancia del coseno:", distancia_coseno)

def euclideandistance(r1, r2):
  # Calcular la distancia euclidiana
  distancia = np.linalg.norm(r2 - r1)

  inver_distancia = 1/distancia

  # Imprimir el resultado
  print(f"La distancia euclidiana entre los vectores {r1} y {r2} es {inver_distancia}")

if __name__ == '__main__':
  matrix = [[5, 3, 4, 4, "-"],
            [3, 1, 2, 3, 3],
            [4, 3, 4, 3, 5],
            [3, 3, 1, 5, 4],
            [1, 5, 5, 2, 1]]

  # Supongamos que tienes dos conjuntos de datos
  data1 = np.array(matrix[0][:-1])
  data2 = np.array(matrix[1][:-1])

  # Calcular la correlación de Pearson
  pearson(data1, data2)

  # Calcular la distancia del coseno
  cosinedistance(data1, data2)

  # Calcular la distancia euclidiana
  euclideandistance(data1, data2)




