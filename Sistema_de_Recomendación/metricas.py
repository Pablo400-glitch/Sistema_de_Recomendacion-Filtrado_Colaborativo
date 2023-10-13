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

if __name__ == '__main__':
  matrix = [[5, 3, 4, 4, "-"],
            [3, 1, 2, 3, 3],
            [4, 3, 4, 3, 5],
            [3, 3, 1, 5, 4],
            [1, 5, 5, 2, 1]]

  user1 = np.array(matrix[0][:-1])
  user2 = np.array(matrix[1][:-1])
  user3 = np.array(matrix[2][:-1])
  user4 = np.array(matrix[3][:-1])

  print(f"Correlacion de Pearson entre {user1} y {user2} =", pearson(user1, user2))

  print(f"Distancia del coseno entre {user1} y {user2}  =", cosine_distance(user1, user2))

  print(f"Distancia euclidiana entre {user1} y {user2}  =", euclidean_distance(user1, user2))

  np.mean([pearson(user1, user2), pearson(user1, user3), pearson(user1, user4)])


