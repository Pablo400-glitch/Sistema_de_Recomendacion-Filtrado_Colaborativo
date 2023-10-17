import sys
from tabulate import tabulate
from termcolor import colored
from utilities import format_data, get_correlations, normalize_matrix, denormalize_matrix, read_file
from prediction import simple_prediction, mean_difference
from menus import metrics_menu, predictions_menu, neighbours_menu

def display_help():
    print("Uso: example.py archivo.txt")
    print("Descripción: Este programa es un sistema recomendador que utiliza métricas para predecir la valoración de un usuario.")
    print("Argumentos:")
    print("  archivo.txt: El archivo que contiene los datos de entrada para el sistema recomendador.")  

def normalize_and_round(data, decimal_places):
  # Se normaliza y desnormaliza la matriz de valoraciones para que los valores estén entre los límites especificados
  data = denormalize_matrix(normalize_matrix(data), float(límite_inferior), float(límite_superior))
  for i in range(len(data)):
      for j in range(len(data[i])):
          data[i][j] = round(data[i][j], decimal_places)

  return data

if __name__ == '__main__':
  if len(sys.argv) == 2 and sys.argv[1] == "--help":
    display_help()
    sys.exit(0)
  elif len(sys.argv) != 2:
    print("Error: Uso incorrecto. Ejecuta 'example.py --help' para obtener ayuda.")
    sys.exit(1)

  file = sys.argv[1]

  límite_inferior, límite_superior, data = read_file(file)

  metrica = metrics_menu()

  prediction = predictions_menu()

  num_neighbours = neighbours_menu(len(data)) 

  # Se itera por cada usuario para predecir sus valoraciones y se almacenan el resultado en la matriz de valoraciones original
  for i in range(len(format_data(data)[1])):
    if prediction == 'Predicción simple':
      simple_prediction(data, format_data(data)[1], get_correlations(format_data(data)[0], data, metrica), num_neighbours)
    elif prediction == 'Diferencia con la media':
      mean_difference(data, format_data(data)[0], format_data(data)[1], get_correlations(format_data(data)[0], data, 'Correlacion de Pearson'), num_neighbours)

  print('\nMatriz de valoraciones')

  data = normalize_and_round(data, 2)

  print(colored(tabulate(data, tablefmt='fancy_grid'),'green'))

  

