import sys
from tabulate import tabulate
from termcolor import colored
import copy
from utilities import format_data, get_correlations, read_file, normalize_denormalize_and_round, restore_data
from prediction import simple_prediction, mean_difference
from menus import metrics_menu, predictions_menu, neighbours_menu

def display_help():
    print(colored("\nUso:","green"))
    print(colored(" example.py archivo.txt","blue"))
    print(colored("Descripción:","green"))
    print(colored(" Este programa es un sistema recomendador que utiliza métricas para predecir la valoración de un usuario.","blue"))
    print(colored("Argumentos:","green"))
    print(colored(" archivo.txt: El archivo que contiene los datos de entrada para el sistema recomendador.","blue"))

if __name__ == '__main__':
  if len(sys.argv) == 2 and sys.argv[1] == "--help":
    display_help()
    sys.exit(0)
  elif len(sys.argv) != 2:
    print(colored("\nError: Uso incorrecto. Ejecuta 'example.py --help' para obtener ayuda.","red"))
    sys.exit(1)

  file = sys.argv[1]

  límite_inferior, límite_superior, data = read_file(file)

  print('\nMatriz de valoraciones incompleta\n')
  print(colored(tabulate(data, tablefmt='fancy_grid'),'yellow'))

  print('\n')
  metric = metrics_menu()

  prediction = predictions_menu()

  num_neighbours = neighbours_menu(len(data)) 

  original_data = copy.deepcopy(data)
  dash_column_original = format_data(original_data)[1]
  dash_row_original = format_data(original_data)[2]

  # Se itera por cada usuario para predecir sus valoraciones y se almacenan el resultado en la matriz de valoraciones original
  for i in range(len(format_data(data)[1])):
    formatted_data = format_data(data)[0]
    dash_column = format_data(data)[1]
    if prediction == 'Predicción simple':
      simple_prediction(data, dash_column, get_correlations(formatted_data, data, metric), num_neighbours)
    elif prediction == 'Diferencia con la media':
      mean_difference(data, formatted_data, dash_column, get_correlations(formatted_data, data, metric), num_neighbours)

  normalized_data = normalize_denormalize_and_round(data, 2, float(límite_inferior), float(límite_superior))

  values = restore_data(original_data, normalized_data, dash_row_original, dash_column_original)

  print('\nMatriz de valoraciones completa\n')
  print(colored(tabulate(original_data, tablefmt='fancy_grid'),'green'))

  print('\nPredicción de valoraciones\n')
  print(colored(tabulate(values, headers=['Usuario', 'Pelicula', 'Valoración'], tablefmt='fancy_grid'),'yellow'))

