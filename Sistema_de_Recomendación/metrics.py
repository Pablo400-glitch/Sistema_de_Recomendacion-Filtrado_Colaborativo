import numpy as np

def pearson(r1, r2):
  return np.corrcoef(r1, r2)[0, 1]

def cosine_distance(r1, r2):
  producto_escalar = np.dot(r1, r2)

  norma_a = np.linalg.norm(r1)
  norma_b = np.linalg.norm(r2)

  return producto_escalar / (norma_a * norma_b)

def euclidean_distance(r1, r2):
  distancia = np.linalg.norm(r2 - r1)

  if (distancia == 0):
    return 0

  return 1 / distancia


