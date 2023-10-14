def are_close(value1, value2, tolerance=1e-9):
    return abs(value1 - value2) < tolerance

def format_data(data):
  column_to_remove = None
  for column in range(len(data[0])):
      if any(row[column] == "-" for row in data):
          column_to_remove = column
          break

  new_matrix = [[row[i] for i in range(len(row)) if i != column_to_remove] for row in data]

  return [new_matrix, column_to_remove]