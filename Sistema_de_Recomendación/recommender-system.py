def pearson():
  print('Correlación de Pearson')

def cosinedistance():
  print('Distancia Coseno')

def euclideandistance():
  print('Distancia Euclidea')

def metricsMenu(m):
  op=1
  metrics = ['Correlación de Pearson', 'Distancia Coseno', 'Distancia Euclidea'] #Lista de opciones
  print('Tipo de métrica\n1.Correlación de Pearson\n2.Distancia Coseno\n3.Distancia Euclidea\n4.Salir') #Muestra las opciones
  op = int(input('Ingresa una opcion: ')) # Usuario ingresa opcion
      
  if op == 1:
    m = metrics[0]
  elif op == 2:
    m = metrics[1]
  elif op == 3:
    m = metrics[2]
  elif op == 4:
    print('Saliendo...')
  else:
    print('Ingrese una opcion valida') 

if __name__ == '__main__':
  m = ""
  metricsMenu(m)