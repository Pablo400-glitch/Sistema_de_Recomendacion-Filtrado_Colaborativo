import sys
from tabulate import tabulate
from termcolor import colored
import copy
from utilities import format_data, get_correlations, read_file, restore_data, normalize_data, denormalize_data
from prediction import simple_prediction, mean_difference

def display_help():
    print(colored("Uso:", "green"))
    print(colored("python recommender_system.py archivo.txt tipo_métrica tipo_predicción número_vecinos", "blue"))
    print(colored("Descripción:", "green"))
    print(colored("Este programa es un sistema recomendador que utiliza métricas y métodos de predicción para ofrecer recomendaciones personalizadas.", "blue"))
    print(colored("Argumentos:", "green"))
    print(colored("1. archivo.txt: El archivo que contiene los datos de entrada para el sistema recomendador.", "blue"))
    print(colored("2. tipo_métrica: El tipo de métrica que se debe utilizar (solo permite números):", "blue"))
    print(colored("     1 - Correlación de Pearson", "blue"))
    print(colored("     2 - Distancia Coseno", "blue"))
    print(colored("     3 - Distancia Euclídea", "blue"))
    print(colored("3. tipo_predicción: El tipo de predicción que se debe utilizar (solo permite números):", "blue"))
    print(colored("     1 - Predicción Simple", "blue"))
    print(colored("     2 - Diferencia con la media", "blue"))
    print(colored("4. número_vecinos: El número de vecinos a considerar en el cálculo de las recomendaciones.", "blue"))

def check_arguments():
  if len(sys.argv) == 2 and sys.argv[1] == "--help":
    display_help()
    sys.exit(0)
  elif len(sys.argv) != 5:
      print(colored("\nError: Uso incorrecto. Ejecuta 'recommender_system.py --help' para obtener ayuda.", "red"))
      sys.exit(1)

  # Validar archivo
  if not sys.argv[1].endswith(".txt"):
      print(colored("\nError: El archivo debe tener extensión '.txt'.", "red"))
      sys.exit(1)

  # Validar tipo de métrica
  if sys.argv[2] not in ["1", "2", "3"]:
      print(colored("\nError: Tipo de métrica no válido. Consulta 'recommender_system.py --help' para obtener ayuda.", "red"))
      sys.exit(1)

  # Validar tipo de predicción
  if sys.argv[3] not in ["1", "2"]:
      print(colored("\nError: Tipo de predicción no válido. Consulta 'recommender_system.py --help' para obtener ayuda.", "red"))
      sys.exit(1)

  # Validar número de vecinos
  if not sys.argv[4].isdigit():
      print(colored("\nError: El número de vecinos debe ser un valor numérico.", "red"))
      sys.exit(1)

  file = sys.argv[1]
  num_metric = sys.argv[2]
  num_prediction = sys.argv[3]
  num_neighbours = sys.argv[4]

  return file, num_metric, num_prediction, num_neighbours

if __name__ == '__main__':
  file, num_metric, num_prediction, num_neighbours = check_arguments()

  num_neighbours = int(num_neighbours)

  límite_inferior, límite_superior, data = read_file(file)

  if num_neighbours >= len(data):
      print(colored("\nError: El número de vecinos debe ser menor que la cantidad de datos.", "red"))
      sys.exit(1)

  allowed_metrics = ['Correlacion de Pearson', 'Distancia Coseno', 'Distancia Euclidea']
  allowed_predictions = ['Predicción simple', 'Diferencia con la media']

  metric = allowed_metrics[int(num_metric) - 1]

  prediction = allowed_predictions[int(num_prediction) - 1]

  print('\nMatriz de valoraciones incompleta\n')
  print(colored(tabulate(data, tablefmt='fancy_grid'),'yellow'))

  original_data = copy.deepcopy(data)
  dash_column_original = format_data(original_data)[1]
  dash_row_original = format_data(original_data)[2]

  # Se itera por cada usuario para predecir sus valoraciones y se almacenan el resultado en la matriz de valoraciones original
  for i in range(len(format_data(data)[1])):
    formatted_data = normalize_data(format_data(data)[0], 0, 1)
    dash_column = format_data(data)[1]
    # Tabla que muestre las correlaciones de cada usuario con los demás
    print(get_correlations(formatted_data, data, metric, num_neighbours))
    print('\nCorrelaciones - Usuario ' + str(format_data(data)[2][0]) + ' - Película ' + str(dash_column[0]))
    print(colored(tabulate(get_correlations(formatted_data, data, metric, num_neighbours), headers=['Usuario', 'Correlación'], tablefmt='fancy_grid'),'blue'))

    if prediction == allowed_predictions[0]:
      simple_prediction(data, dash_column, get_correlations(formatted_data, data, metric, num_neighbours))
    elif prediction == allowed_predictions[1]:
      print(mean_difference(data, formatted_data, dash_column, get_correlations(formatted_data, data, metric, num_neighbours)))

  #values = restore_data(original_data, data, dash_row_original, dash_column_original, float(límite_inferior), float(límite_superior))

  for row in data:
     print(row)

  denormalized_data = denormalize_data(data, float(límite_inferior), float(límite_superior))

  print('\nMatriz de valoraciones completa\n')
  print(colored(tabulate(denormalized_data, tablefmt='fancy_grid'),'green'))

  #print('\nPredicción de valoraciones\n')
  #print(colored(tabulate(denormalized_data, headers=['Usuario', 'Pelicula', 'Valoración'], tablefmt='fancy_grid'),'yellow'))

