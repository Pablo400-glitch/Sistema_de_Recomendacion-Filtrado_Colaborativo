from termcolor import colored

def metrics_menu():
    metricas_disponibles = ['Correlacion de Pearson', 'Distancia Coseno', 'Distancia Euclidea']
    print(colored("Elige una métrica:", 'green'))
    for i, metrica in enumerate(metricas_disponibles):
        print(colored(f"{i + 1}. {metrica}", 'cyan'))
    
    while True:
        try:
            seleccion = int(input(colored("Ingrese el número de la métrica deseada: ", 'yellow')))
            if 1 <= seleccion <= len(metricas_disponibles):
                seleccion_metrica = metricas_disponibles[seleccion - 1]
                mensaje = "Has seleccionado: "
                print(colored("\n" + mensaje, 'green') + colored(seleccion_metrica + "\n", 'magenta'))
                return seleccion_metrica
            else:
                print(colored("Opción no válida. Por favor, seleccione un número válido.", 'red'))
        except ValueError:
            print(colored("Opción no válida. Por favor, seleccione un número válido.", 'red'))

def predictions_menu():
    predicciones_disponibles = ['Predicción simple', 'Diferencia con la media']
    print(colored("Elige una predicción:", 'green'))
    for i, prediccion in enumerate(predicciones_disponibles):
        print(colored(f"{i + 1}. {prediccion}", 'cyan'))
    
    while True:
        try:
            seleccion = int(input(colored("Ingrese el número de la predicción deseada: ", 'yellow')))
            if 1 <= seleccion <= len(predicciones_disponibles):
                seleccion = predicciones_disponibles[seleccion - 1]
                mensaje = "Has seleccionado: "
                print(colored("\n" + mensaje, 'green') + colored(seleccion + "\n", 'magenta'))
                return seleccion
            else:
                print(colored("Opción no válida. Por favor, seleccione un número válido.", 'red'))
        except ValueError:
            print(colored("Opción no válida. Por favor, seleccione un número válido.", 'red'))

def neighbours_menu(num_neighbours):
    while True:
        try:
            num_vecinos = int(input(colored(f"Ingrese el número de vecinos (menor que {num_neighbours}): ", 'yellow')))
            if 1 <= num_vecinos < num_neighbours:
                return num_vecinos
            else:
                print(colored(f"El número de vecinos debe ser un valor válido y menor que {num_neighbours}.", 'red'))
        except ValueError:
            print(colored("Entrada no válida. Por favor, ingrese un número válido.", 'red'))
