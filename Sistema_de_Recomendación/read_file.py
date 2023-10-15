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
      límite_inferior = archivo.readline().strip()

      límite_superior = archivo.readline().strip()

      for linea in archivo:
          elementos = linea.split()
          elementos = [float(e) if e != '-' else "-" for e in elementos]
          matriz.append(elementos)

      print("Límite Inferior:", límite_inferior)
      print("Límite Superior:", límite_superior)

      for fila in matriz:
          print(fila)