import sys
from utilities import format_data, get_correlations, normalize_matrix, denormalize_matrix, read_file
from prediction import simple_prediction, mean_difference
from menus import metrics_menu, predictions_menu, neighbours_menu

def display_help():
    print("Uso: example.py archivo.txt")
    print("Descripción: Este programa es un sistema recomendador que utiliza métricas para predecir la valoración de un usuario.")
    print("Argumentos:")
    print("  archivo.txt: El archivo que contiene los datos de entrada para el sistema recomendador.")  

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

  for i in range(len(format_data(data)[1])):
    if prediction == 'Predicción simple':
      simple_prediction(data, format_data(data)[1], get_correlations(format_data(data)[0], data, metrica), num_neighbours)
    elif prediction == 'Diferencia con la media':
      mean_difference(data, format_data(data)[0], format_data(data)[1], get_correlations(format_data(data)[0], data, 'Correlacion de Pearson'), num_neighbours)

  data = denormalize_matrix(normalize_matrix(data), float(límite_inferior), float(límite_superior))

  print('\nMatriz de valoraciones: \n')
  for row in data:
    formatted_row = [round(value, 4) for value in row]
    print(formatted_row)




