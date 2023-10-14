from prediction import get_correlations

def format_data(data):
  rows_to_remove = []

  for row in data:
    if "-" in row:
      rows_to_remove.append(row)

  # Encuentra las columnas a eliminar
  columns_to_remove = list()
  for row in rows_to_remove:
    for i, element in enumerate(row):
      if element == "-":
        columns_to_remove.append(i)

  new_matrix = [[row[i] for i in range(len(row)) if i not in columns_to_remove] for row in data]

  return [new_matrix, columns_to_remove]

if __name__ == '__main__':
  matrix = [[5, 3, 4, 4, "-"],
            [3, 1, 2, 3, 3],
            [4, 3, 4, 3, 5],
            [3, 3, 1, 5, 4],
            [1, 5, 5, 2, 1]]
  
  data = [
    [3, 5, 0, 1, 4, 5, 5, 1, 2, 4, 0, 0, 1, 4, 1, 3, 2, 4, 1, 1, 5, "-", 5, 2, 0],
    [4, 5, 1, 3, 4, 2, 0, 1, 4, "-", 0, 2, "-", 2, 0, 1, 4, 5, 3, "-", 1, 0, 5, "-", 0],
    [2, 5, 1, 1, 1, 3, 2, 4, 5, 3, 4, 1, 1, 3, "-", 1, 5, "-", 5, 5, 4, 1, 1, 5, 5],
    [3, 5, 1, 4, 1, 2, 3, "-", 5, 5, 2, 5, 1, 5, 3, 2, 3, 3, 1, 3, 1, 5, 5, "-", 3],
    [5, 1, 0, 3, 0, 0, 5, 0, 4, 2, 3, 1, 5, 4, 5, 4, 2, 5, 3, 3, "-", 3, 3, 5, 0],
    [2, 4, 3, 3, 0, 0, 0, 2, 0, 5, 2, 0, 4, 2, 1, 5, 3, 4, 3, 1, 3, 2, 5, 0, 2],
    [1, 5, 1, 5, 1, 5, 1, "-", 5, 5, 0, 2, 1, 1, "-", 5, 0, 3, 1, 3, "-", 2, 5, 2, 3],
    [4, 1, 1, 3, "-", 2, 1, 1, 5, 2, 0, 1, 1, 5, 0, 0, 4, 5, 2, 3, 0, "-", 1, 3, 5],
    [1, 5, 0, 1, 1, 0, 3, 2, 0, 5, 2, 1, 2, "-", 3, 3, 5, 1, 2, "-", 5, 3, 5, 3, 1],
    [1, 0, 2, 5, 1, 5, 1, 2, 2, 2, 2, 3, 4, 5, 2, 5, 3, 3, 3, 0, 3, 3, 4, 4, 2]
  ]
  
  print(format_data(data)[1])
  print(get_correlations(format_data(data)[0], 'Correlacion de Pearson'))