import numpy as np
from utilities import find_dash, check_rate, get_correlations

def simple_prediction(original_matrix, dash, correlations, num_neighbors):
  sum_num = 0
  sum_denom = 0
  correlations = correlations[:num_neighbors]

  dash_row = find_dash(original_matrix)

  # Arreglar esto
  for corr in correlations:
    if (original_matrix[corr[1]][dash[0]] == "-"):
      continue
    else:
      sum_num += corr[0] * original_matrix[corr[1]][dash[0]]
  
  for corr in correlations:
    sum_denom += corr[0]

  original_matrix[dash_row][dash[0]] = round((sum_num / sum_denom), 4);

  original_matrix[dash_row][dash[0]] = check_rate(original_matrix[dash_row][dash[0]], 5, 0)

  return sum_num / sum_denom

def mean_difference(original_matrix, formatted_matrix, dash, correlations, num_neighbors):
  sum_num = 0
  sum_denom = 0
  correlations = correlations[:num_neighbors]

  dash_row = find_dash(original_matrix)

  for corr in correlations:
    if (original_matrix[corr[1]][dash[0]] == "-"):
      continue
    else:
      sum_num += corr[0] * (original_matrix[corr[1]][dash[0]] - np.mean(formatted_matrix[corr[1]]))

  for corr in correlations:
    sum_denom += corr[0]

  original_matrix[dash_row][dash[0]] = round(np.mean(formatted_matrix[0][dash_row]) + (sum_num / sum_denom), 4);

  original_matrix[dash_row][dash[0]] = check_rate(original_matrix[dash_row][dash[0]], 5, 0)

  return original_matrix[dash_row][dash[0]]