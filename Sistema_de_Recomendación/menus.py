def metrics_menu():
  metricas_disponibles = ['Correlacion de Pearson', 'Distancia Coseno', 'Distancia Euclidea']
  print("Elige una métrica:")
  for i, metrica in enumerate(metricas_disponibles):
    print(f"{i + 1}. {metrica}")
    
  while True:
    try:
      seleccion = int(input("Ingrese el número de la métrica deseada: "))
      if 1 <= seleccion <= len(metricas_disponibles):
        print(f"\nHas seleccionado: {metricas_disponibles[seleccion - 1]}\n")
        return metricas_disponibles[seleccion - 1]
      else:
        print("Opción no válida. Por favor, seleccione un número válido.")
    except ValueError:
      print("Opción no válida. Por favor, seleccione un número válido.")

def predictions_menu():
    predicciones_disponibles = ['Predicción simple', 'Diferencia con la media']
    print("Elige una predicción:")
    for i, prediccion in enumerate(predicciones_disponibles):
        print(f"{i + 1}. {prediccion}")
    
    while True:
        try:
            seleccion = int(input("Ingrese el número de la predicción deseada: "))
            if 1 <= seleccion <= len(predicciones_disponibles):
                  print(f"\nHas seleccionado: {predicciones_disponibles[seleccion - 1]}\n")
                  return predicciones_disponibles[seleccion - 1]
            else:
                print("Opción no válida. Por favor, seleccione un número válido.")
        except ValueError:
            print("Opción no válida. Por favor, seleccione un número válido.")

def neighbours_menu(num_neighbours):
    while True:
        try:
            num_vecinos = int(input(f"Ingrese el número de vecinos (menor que {num_neighbours}): "))
            if 1 <= num_vecinos < num_neighbours:
                return num_vecinos
            else:
                print(f"El número de vecinos debe ser un valor válido y menor que {num_neighbours}.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número válido.")