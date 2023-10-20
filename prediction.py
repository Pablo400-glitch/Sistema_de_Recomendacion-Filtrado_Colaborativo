import numpy as np

def simple_prediction(original_data, dash_column, dash_row, correlations):
  sum_num = 0
  sum_denom = 0

  # Arreglar esto
  for corr in correlations:
    if (original_data[corr[0]][dash_column[0]] == "-"):
      continue
    else:
      sum_num += corr[1] * original_data[corr[0]][dash_column[0]]
  
  for corr in correlations:
    sum_denom += corr[1]

  original_data[dash_row[0]][dash_column[0]] = round((sum_num / sum_denom), 4);

  return original_data[dash_row[0]][dash_column[0]]

def mean_difference(original_data, formatted_data, dash_column, dash_row, correlations):
  sum_num = 0
  sum_denom = 0

  for corr in correlations:
    if (original_data[corr[0]][dash_column[0]] == "-"):
      continue
    else:
      sum_num += corr[1] * (original_data[corr[0]][dash_column[0]] - np.mean(formatted_data[corr[0]]))    

  for corr in correlations:
    sum_denom += corr[1]

  original_data[dash_row[0]][dash_column[0]] = round(np.mean(formatted_data[dash_row]) + (sum_num / sum_denom), 4);

  return original_data[dash_row[0]][dash_column[0]]