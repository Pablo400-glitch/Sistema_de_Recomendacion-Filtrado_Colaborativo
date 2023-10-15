import numpy as np
from prediction import simple_prediction, mean_difference
from utilities import format_data, get_correlations

if __name__ == '__main__':
  data = [
    [4, 5, 1, 3, 4, 2, 0, 1, 4, "-", 0, 2, "-", 2, 0, 1, 4, 5, 3, "-", 1, 0, 5, "-", 0],
    [3, 5, 0, 1, 4, 5, 5, 1, 2, 4, 0, 0, 1, 4, 1, 3, 2, 4, 1, 1, 5, "-", 5, 2, 0],
    [2, 5, 1, 1, 1, 3, 2, 4, 5, 3, 4, 1, 1, 3, "-", 1, 5, "-", 5, 5, 4, 1, 1, 5, 5],
    [3, 5, 1, 4, 1, 2, 3, "-", 5, 5, 2, 5, 1, 5, 3, 2, 3, 3, 1, 3, 1, 5, 5, "-", 3],
    [5, 1, 0, 3, 0, 0, 5, 0, 4, 2, 3, 1, 5, 4, 5, 4, 2, 5, 3, 3, "-", 3, 3, 5, 0],
    [2, 4, 3, 3, 0, 0, 0, 2, 0, 5, 2, 0, 4, 2, 1, 5, 3, 4, 3, 1, 3, 2, 5, 0, 2],
    [1, 5, 1, 5, 1, 5, 1, "-", 5, 5, 0, 2, 1, 1, "-", 5, 0, 3, 1, 3, "-", 2, 5, 2, 3],
    [4, 1, 1, 3, "-", 2, 1, 1, 5, 2, 0, 1, 1, 5, 0, 0, 4, 5, 2, 3, 0, "-", 1, 3, 5],
    [1, 5, 0, 1, 1, 0, 3, 2, 0, 5, 2, 1, 2, "-", 3, 3, 5, 1, 2, "-", 5, 3, 5, 3, 1],
    [1, 0, 2, 5, 1, 5, 1, 2, 2, 2, 2, 3, 4, 5, 2, 5, 3, 3, 3, 0, 3, 3, 4, 4, 2]
  ]

  print("Correlacion de Pearson")
  for i in range(len(get_correlations(format_data(data)[0], data, 'Correlacion de Pearson'))):
    print(get_correlations(format_data(data)[0], data, 'Correlacion de Pearson')[i])
  
  print("\nDistancia Coseno")
  for i in range(len(get_correlations(format_data(data)[0], data, 'Distancia Coseno'))):
    print(get_correlations(format_data(data)[0], data, 'Distancia Coseno')[i])
  print("\nDistancia Euclidea")
  for i in range(len(get_correlations(format_data(data)[0], data, 'Distancia Euclidea'))):
    print(get_correlations(format_data(data)[0], data, 'Distancia Euclidea')[i])

  for i in range(len(format_data(data)[1])):
    simple_prediction(data, format_data(data)[1],get_correlations(format_data(data)[0], data, 'Correlacion de Pearson'), 2)
  
  print('\nMatrix con predicciones simples')
  for row in data:
    print(row)

  #for i in range(len(format_data(data)[1])):
  #  mean_difference(data, format_data(data)[0], format_data(data)[1], get_correlations(format_data(data)[0], data, 'Correlacion de Pearson'), 2)

  #print('\nMatrix con predicciones por diferencia de medias')
  #for row in data:
    #print(row)