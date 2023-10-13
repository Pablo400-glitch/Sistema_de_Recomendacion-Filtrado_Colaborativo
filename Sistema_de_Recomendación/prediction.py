import numpy as np
from metricas import pearson, cosine_distance, euclidean_distance

def format_data(data):
  column_to_remove = None
  for column in range(len(data[0])):
      if any(row[column] == "-" for row in data):
          column_to_remove = column
          break

  new_matrix = [[row[i] for i in range(len(row)) if i != column_to_remove] for row in data]

  return [new_matrix, column_to_remove]

def get_correlations(data, metric):
  correlations = []
  new_correlations = []

  for i in range(len(data)):
    if metric == 'Correlacion de Pearson':
      correlations.append([pearson(np.array(data[0]), np.array(data[i])), int(i)])
    elif metric == 'Distancia Coseno':
      correlations.append([cosine_distance(np.array(data[0]), np.array(data[i])), int(i)])
    elif metric == 'Distancia Euclidea':
        correlations.append([euclidean_distance(np.array(data[0]), np.array(data[i])), int(i)])

  for item in correlations:
    if item[0] != 1.0:
        new_correlations.append(item)

  return sorted(new_correlations, reverse=True)

def simple_prediction(original_matrix, stripe, correlations, num_neighbors):
  sum_num = 0
  sum_denom = 0
  correlations = correlations[:num_neighbors]

  for corr in correlations:
    sum_num += corr[0] * original_matrix[corr[1]][stripe]
  
  for corr in correlations:
    sum_denom += corr[0]

  return sum_num / sum_denom

def mean_difference(original_matrix, formatted_matrix, stripe, correlations, num_neighbors):
  sum_num = 0
  sum_denom = 0
  correlations = correlations[:num_neighbors]

  for i in range(len(original_matrix)):
    if original_matrix[i][stripe] == "-":
      stripe_pos = original_matrix[i][stripe].index("-")

  for corr in correlations:
    sum_num += corr[0] * (original_matrix[corr[1]][stripe] - np.mean(original_matrix[corr[1]]))

  for corr in correlations:
    sum_denom += corr[0]

  return np.mean(formatted_matrix[0][stripe_pos]) + (sum_num / sum_denom)

if __name__ == '__main__':
  matrix = [[5, 3, 4, 4, "-"],
            [3, 1, 2, 3, 3],
            [4, 3, 4, 3, 5],
            [3, 3, 1, 5, 4],
            [1, 5, 5, 2, 1]]

  #print(get_correlations(format_data(matrix)[0], 'Correlacion de Pearson'))
  #print(simple_prediction(matrix, format_data(matrix)[1],get_correlations(format_data(matrix)[0], 'Correlacion de Pearson'), 2))
  print(mean_difference(matrix, format_data(matrix), format_data(matrix)[1],get_correlations(format_data(matrix)[0], 'Correlacion de Pearson'), 2))