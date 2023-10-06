import numpy as np

def simplePrediction():
  print('Predicción simple')


if __name__ == '__main__':
  matrix = [[5, 3, 4, 4, "-"],
            [3, 1, 2, 3, 3],
            [4, 3, 4, 3, 5],
            [3, 3, 1, 5, 4],
            [1, 5, 5, 2, 1]]

  # Supongamos que tienes dos conjuntos de datos
  data1 = np.array(matrix[0][:-1])
  data2 = np.array(matrix[1][:-1])