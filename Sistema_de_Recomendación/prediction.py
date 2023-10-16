import numpy as np
from utilities import find_dash, get_correlations

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

  return original_matrix[dash_row][dash[0]]

def mean_difference(original_matrix, formatted_matrix, dash, correlations, num_neighbors):
  sum_num = 0
  sum_denom = 0
  correlations = correlations[:num_neighbors - 1]

  dash_row = find_dash(original_matrix)

  for corr in correlations:
    if (original_matrix[corr[1]][dash[0]] == "-"):
      continue
    else:
      sum_num += corr[0] * (original_matrix[corr[1]][dash[0]] - np.mean(formatted_matrix[corr[1]]))    

  for corr in correlations:
    sum_denom += corr[0]

  original_matrix[dash_row][dash[0]] = round(np.mean(formatted_matrix[dash_row]) + (sum_num / sum_denom), 4);

  return original_matrix[dash_row][dash[0]]