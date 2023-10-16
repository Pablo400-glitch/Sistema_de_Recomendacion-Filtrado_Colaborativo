import numpy as np
import sys
from prediction import simple_prediction, mean_difference
from utilities import format_data, get_correlations, normalize_matrix, denormalize_matrix, read_file

if __name__ == '__main__':
  file = sys.argv[1]

  límite_inferior = 0.000
  límite_superior = 0.000
  data = []

  límite_inferior, límite_superior, data = read_file(file)

  '''
  print("Correlacion de Pearson")
  for i in range(len(get_correlations(format_data(data)[0], data, 'Correlacion de Pearson'))):
    print(get_correlations(format_data(data)[0], data, 'Correlacion de Pearson')[i])
  
  print("\nDistancia Coseno")
  for i in range(len(get_correlations(format_data(data)[0], data, 'Distancia Coseno'))):
    print(get_correlations(format_data(data)[0], data, 'Distancia Coseno')[i])
  print("\nDistancia Euclidea")
  for i in range(len(get_correlations(format_data(data)[0], data, 'Distancia Euclidea'))):
    print(get_correlations(format_data(data)[0], data, 'Distancia Euclidea')[i])
  '''
  #for i in range(len(format_data(data)[1])):
  #  simple_prediction(data, format_data(data)[1],get_correlations(format_data(data)[0], data, 'Correlacion de Pearson'), 2)

  for i in range(len(format_data(data)[1])):
    mean_difference(data, format_data(data)[0], format_data(data)[1], get_correlations(format_data(data)[0], data, 'Correlacion de Pearson'), 3)

  data = denormalize_matrix(normalize_matrix(data), float(límite_inferior), float(límite_superior))
  
  for row in data:
    formatted_row = [round(value, 4) for value in row]
    print(formatted_row)
  
  