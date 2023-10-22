import sys
from tabulate import tabulate
from termcolor import colored
import copy
from utilities import format_data, get_correlations, read_file, users_rating, normalize_data, denormalize_data
from prediction import simple_prediction, mean_difference

def display_help():
    print(colored("\nUso:", "green"))
    print(colored("python recommender_system.py -a <nombre_archivo>.txt -m <tipo_métrica> -p <tipo_predicción> -v <número_vecinos>\n", "blue"))
    print(colored("Descripción:", "green"))
    print(colored("Este programa es un sistema recomendador que utiliza métricas y métodos de predicción para ofrecer recomendaciones personalizadas.\n", "blue"))
    print(colored("Argumentos:", "green"))
    print(colored("-a, --archivo: El archivo que contiene los datos de entrada para el sistema recomendador.", "blue"))
    print(colored("               Ejemplo: -a datos.txt\n", "blue"))
    print(colored("-m, --metrica: El tipo de métrica que se debe utilizar (solo permite números):", "blue"))
    print(colored("<tipo_métrica>:", "blue"))
    print(colored("     1 - Correlación de Pearson", "blue"))
    print(colored("     2 - Distancia Coseno", "blue"))
    print(colored("     3 - Distancia Euclídea", "blue"))
    print(colored("         Ejemplo: -m 1\n", "blue"))
    print(colored("-p, --prediccion: El tipo de predicción que se debe utilizar (solo permite números):", "blue"))
    print(colored("<tipo_predicción>:", "blue"))
    print(colored("     1 - Predicción Simple", "blue"))
    print(colored("     2 - Diferencia con la media", "blue"))
    print(colored("         Ejemplo: -p 2\n", "blue"))
    print(colored("-v, --vecinos: El número de vecinos a considerar en el cálculo de las recomendaciones.", "blue"))
    print(colored("               Ejemplo: -v 5", "blue"))


def check_arguments():
    if len(sys.argv) == 2 and sys.argv[1] == "--help":
        display_help()
        sys.exit(0)
    elif len(sys.argv) != 9:
        print(colored("\nError: Uso incorrecto. Ejecuta 'recommender_system.py --help' para obtener ayuda.\n", "red"))
        sys.exit(1)

    # Validar archivo
    archivo_option_index = sys.argv.index('-a')
    archivo = sys.argv[archivo_option_index + 1]

    if not archivo.endswith(".txt"):
        print(colored("\nError: El archivo debe tener extensión '.txt'.\n", "red"))
        sys.exit(1)

    # Validar tipo de métrica
    metrica_option_index = sys.argv.index('-m')
    num_metric = sys.argv[metrica_option_index + 1]

    if num_metric not in ["1", "2", "3"]:
        print(colored("\nError: Tipo de métrica no válido. Consulta 'recommender_system.py --help' para obtener ayuda.\n", "red"))
        sys.exit(1)

    # Validar tipo de predicción
    prediccion_option_index = sys.argv.index('-p')
    num_prediction = sys.argv[prediccion_option_index + 1]

    if num_prediction not in ["1", "2"]:
        print(colored("\nError: Tipo de predicción no válido. Consulta 'recommender_system.py --help' para obtener ayuda.\n", "red"))
        sys.exit(1)

    # Validar número de vecinos
    vecinos_option_index = sys.argv.index('-v')
    num_neighbours = sys.argv[vecinos_option_index + 1]

    if not num_neighbours.isdigit():
        print(colored("\nError: El número de vecinos debe ser un valor numérico.\n", "red"))
        sys.exit(1)

    return archivo, num_metric, num_prediction, num_neighbours

if __name__ == '__main__':
  file, num_metric, num_prediction, num_neighbours = check_arguments()

  num_neighbours = int(num_neighbours)

  límite_inferior, límite_superior, data = read_file(file)

  if num_neighbours >= len(data) or num_neighbours < 1:
      print(colored("\nError: El número de vecinos debe ser menor que la cantidad de datos o mayor que 1.\n", "red"))
      sys.exit(1)

  allowed_metrics = ['Correlacion de Pearson', 'Distancia Coseno', 'Distancia Euclidea']
  allowed_predictions = ['Predicción simple', 'Diferencia con la media']

  metric = allowed_metrics[int(num_metric) - 1]

  prediction = allowed_predictions[int(num_prediction) - 1]

  original_data = copy.deepcopy(data)
  dash_column_original = format_data(original_data)[1]
  dash_row_original = format_data(original_data)[2]

  # Se itera por cada usuario para predecir sus valoraciones y se almacenan el resultado en la matriz de valoraciones original
  for i in range(len(format_data(data)[1])):
    formatted_data = normalize_data(format_data(data)[0], 0, 1)
    dash_column = format_data(data)[1]
    dash_row = format_data(data)[2]
    correlations = get_correlations(formatted_data, dash_row, metric, num_neighbours)
    
    print('\n' + metric +' - Usuario ' + str(format_data(data)[2][0]) + ' - Película ' + str(dash_column[0]))
    print(colored(tabulate(correlations, headers=['Usuario', 'Correlación'], tablefmt='fancy_grid'),'blue'))

    if prediction == allowed_predictions[0]:
      simple_prediction(data, dash_column, dash_row, correlations)
    elif prediction == allowed_predictions[1]:
      mean_difference(data, formatted_data, dash_column, dash_row, correlations)

  denormalized_data = denormalize_data(data, float(límite_inferior), float(límite_superior))

  values = users_rating(original_data, denormalized_data)

  print('\nMatriz de valoraciones incompleta\n')
  print(colored(tabulate(original_data, tablefmt='fancy_grid'),'yellow'))

  print('\nMatriz de valoraciones completa\n')
  print(colored(tabulate(denormalized_data, tablefmt='fancy_grid'),'green'))

  print('\nPredicción de valoraciones\n')
  print(colored(tabulate(values, headers=['Usuario', 'Pelicula', 'Valoración'], tablefmt='fancy_grid'),'yellow'))

