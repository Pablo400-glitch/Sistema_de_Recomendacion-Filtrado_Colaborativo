def read_file(file_name):
  users = []
  i = 0
  for line in file_name:
    users[i] = line
    
if __name__ == '__main__':
  archivo = open("users.txt", "r")

  file_name = "users.txt"

  límite_inferior = None
  límite_superior = None
  matriz = []

  with open(file_name, "r") as archivo:
      # Lee la primera línea
      límite_inferior = archivo.readline().strip()

      # Lee la segunda línea
      límite_superior = archivo.readline().strip()

      # Lee el resto de líneas y las almacena en la matriz
      for linea in archivo:
          elementos = linea.split()
          elementos = [float(e) if e != '-' else None for e in elementos]
          matriz.append(elementos)

      # Imprime las dos primeras líneas
      print("Límite Inferior:", límite_inferior)
      print("Límite Superior:", límite_superior)

      # Imprime la matriz
      for fila in matriz:
          print(fila)