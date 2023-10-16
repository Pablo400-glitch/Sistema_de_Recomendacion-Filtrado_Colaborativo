import numpy as np
from metrics import pearson, cosine_distance, euclidean_distance

def format_data(data):
  rows_to_remove = []

  for row in data:
    if "-" in row:
      rows_to_remove.append(row)

  # Encuentra las columnas a eliminar
  columns_to_remove = list()
  for row in rows_to_remove:
    for i, element in enumerate(row):
      if element == "-":
        columns_to_remove.append(i)

  new_matrix = [[row[i] for i in range(len(row)) if i not in columns_to_remove] for row in data]

  return [new_matrix, columns_to_remove]

def get_correlations(data, original_matrix, metric):
  correlations = []
  new_correlations = []

  dash_row = find_dash(original_matrix)

  for i in range(len(data)):
    if (dash_row == None):
      break

    if (dash_row == i):
      continue
    else:
      if metric == 'Correlacion de Pearson':
          correlations.append([pearson(np.array(data[dash_row]), np.array(data[i])), int(i)])
      elif metric == 'Distancia Coseno':
          correlations.append([cosine_distance(np.array(data[dash_row]), np.array(data[i])), int(i)])
      elif metric == 'Distancia Euclidea':
        correlations.append([euclidean_distance(np.array(data[dash_row]), np.array(data[i])), int(i)])

  if metric == 'Correlacion de Pearson':
    for item in correlations:
      if item[0] != 1.0:
        new_correlations.append(item)
    new_correlations = sorted(new_correlations, reverse=True)
  elif metric == 'Distancia Coseno':
    new_correlations = sorted(correlations, reverse=True)
  elif metric == 'Distancia Euclidea':
    for item in correlations:
      if item[0] != 0.0:
        new_correlations.append(item)
    new_correlations = sorted(new_correlations, reverse=False)

  return new_correlations

def find_dash(matrix):
    for row, row_values in enumerate(matrix):
        if "-" in row_values:
            return row
    return None

# Normalizar la matriz al rango 0-1
def normalize_matrix(matrix):
    min_original = np.min(matrix)
    max_original = np.max(matrix)
    normalized_matrix = (matrix - min_original) / (max_original - min_original)
    
    return normalized_matrix

def denormalize_matrix(normalized_matrix, min_original, max_original):
    # Desnormalizar la matriz al rango especificado
    denormalized_matrix = (normalized_matrix * (max_original - min_original)) + min_original
    
    return denormalized_matrix

def read_file(file_name):
  límite_inferior = None
  límite_superior = None
  data = []

  file = open(file_name, "r")
  with file as archivo:
    límite_inferior = archivo.readline().strip()
    límite_superior = archivo.readline().strip()

    for linea in archivo:
      elementos = linea.split()
      elementos = [float(e) if e != '-' else "-" for e in elementos]
      data.append(elementos)

  return límite_inferior, límite_superior, data

