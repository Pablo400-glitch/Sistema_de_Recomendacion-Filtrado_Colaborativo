import numpy as np
from utilities import find_dash

def simple_prediction(original_data, dash_column, correlations, num_neighbors):
  sum_num = 0
  sum_denom = 0
  correlations = correlations[:num_neighbors - 1]

  dash_row = find_dash(original_data)

  # Arreglar esto
  for corr in correlations:
    if (original_data[corr[1]][dash_column[0]] == "-"):
      continue
    else:
      sum_num += corr[0] * original_data[corr[1]][dash_column[0]]
  
  for corr in correlations:
    sum_denom += corr[0]

  original_data[dash_row][dash_column[0]] = round((sum_num / sum_denom), 4);

  return original_data[dash_row][dash_column[0]]

def mean_difference(original_data, formatted_data, dash_column, correlations, num_neighbors):
  sum_num = 0
  sum_denom = 0
  correlations = correlations[:num_neighbors - 1]

  dash_row = find_dash(original_data)

  for corr in correlations:
    if (original_data[corr[1]][dash_column[0]] == "-"):
      continue
    else:
      sum_num += corr[0] * (original_data[corr[1]][dash_column[0]] - np.mean(formatted_data[corr[1]]))    

  for corr in correlations:
    sum_denom += corr[0]

  original_data[dash_row][dash_column[0]] = round(np.mean(formatted_data[dash_row]) + (sum_num / sum_denom), 4);

  return original_data[dash_row][dash_column[0]]