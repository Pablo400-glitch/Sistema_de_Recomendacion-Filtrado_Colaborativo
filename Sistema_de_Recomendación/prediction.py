import numpy as np
from metricas import pearson, cosine_distance, euclidean_distance

def format_data(data):
  column_to_remove = None
  for column in range(len(data[0])):
      if any(row[column] == "-" for row in data):
          column_to_remove = column
          break

  new_matrix = [[row[i] for i in range(len(row)) if i != column_to_remove] for row in data]

  return new_matrix

def get_correlations(data, metric):
  correlations = []
  new_correlations = []

  for i in range(len(data)):
    if metric == 'Correlacion de Pearson':
      correlations.append([pearson(data[0], data[i]), "Usuario " + str(i + 1)])
    elif metric == 'Distancia Coseno':
      correlations.append([cosine_distance(data[0], data[i]), "Usuario " + str(i + 1)])
    elif metric == 'Distancia Euclidea':
      correlations.append([euclidean_distance(data[0], data[i]), "Usuario " + str(i + 1)])

  for item in correlations:
    if item[0] != 1.0:
        new_correlations.append(item)

  return sorted(new_correlations, reverse=True)

#def simplePrediction(num_neighbors):

if __name__ == '__main__':
  matrix = [[5, 3, 4, 4, "-"],
            [3, 1, 2, 3, 3],
            [4, 3, 4, 3, 5],
            [3, 3, 1, 5, 4],
            [1, 5, 5, 2, 1]]

  print(get_correlations(format_data(matrix), 'Correlacion de Pearson'))