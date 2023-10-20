import numpy as np
from metrics import pearson, cosine_distance, euclidean_distance

def format_data(data):
  rows_to_remove = list()
  row_position = list()

  for row in data:
    if "-" in row:
      row_position.append(data.index(row))
      rows_to_remove.append(row)

  # Encuentra las columnas a eliminar
  columns_to_remove = list()
  for row in rows_to_remove:
    for i, element in enumerate(row):
      if element == "-":
        columns_to_remove.append(i)

  new_matrix = [[row[i] for i in range(len(row)) if i not in columns_to_remove] for row in data]

  return [new_matrix, columns_to_remove, row_position]

def get_correlations(data, dash_row, metric, num_neighbors):
  correlations = []
  new_correlations = []

  for i in range(len(data)):
    if (dash_row[0] == None):
      break

    if (dash_row[0] == i):
      continue
    else:
      if len(correlations) == num_neighbors:
        break
      if metric == 'Correlacion de Pearson':
          correlations.append([int(i), pearson(np.array(data[dash_row[0]]), np.array(data[i]))])
      elif metric == 'Distancia Coseno':
          correlations.append([int(i), cosine_distance(np.array(data[dash_row[0]]), np.array(data[i]))])
      elif metric == 'Distancia Euclidea':
        correlations.append([int(i), euclidean_distance(np.array(data[dash_row[0]]), np.array(data[i]))])

  if metric == 'Correlacion de Pearson':
    for item in correlations:
      if item[1] != 1.0:
        new_correlations.append(item)
    new_correlations = sorted(new_correlations, key=lambda x: x[1], reverse=True)
  elif metric == 'Distancia Coseno':
    new_correlations = sorted(correlations, key=lambda x: x[1], reverse=True)
  elif metric == 'Distancia Euclidea':
    for item in correlations:
      if item[1] != 0.0:
        new_correlations.append(item)
    new_correlations = sorted(new_correlations, key=lambda x: x[1], reverse=False)

  return new_correlations

# Normalizar la matriz al rango 0-1
def normalize_data(data, new_min, new_max):
    min_original = np.min(data)
    max_original = np.max(data)
    normalized_data = (data - min_original) / (max_original - min_original)
    # Escalamos los datos normalizados al nuevo rango [new_min, new_max]
    normalized_data = normalized_data * (new_max - new_min) + new_min
    
    return normalized_data

def denormalize_data(normalized_data, min_original, max_original):
    min_original = np.min(normalized_data)
    max_original = np.max(normalized_data)
    normalized_data = (normalized_data - min_original) / (max_original - min_original)
    # Escalamos los datos normalizados al nuevo rango [new_min, new_max]
    denormalized_data = normalized_data * (max_original - min_original) + min_original
    
    return denormalized_data

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

def users_rating(original_data, normalized_data):
  values = []
  for row in range(len(original_data)):
    for column in range(len(original_data[row])):
      if original_data[row][column] == "-":
        values.append([row + 1, column + 1, normalized_data[row][column]])
  
  return values
