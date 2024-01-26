import math

def array_convert(array, num):
  array_length = len(array)
  square_root = math.sqrt(num)

  # Check if the array can be converted into a square matrix of size num.
  if array_length != num or not square_root.is_integer():
    return f"This array cannot be converted into a square matrix of size {num}"

  # Convert the array into a 2D matrix.
  matrix = [[0] * int(square_root) for _ in range(int(square_root))]
  index = 0
  for i in range(int(square_root)):
    for j in range(int(square_root)):
      matrix[i][j] = array[index]
      index += 1

  return matrix

print(array_convert([1,2,3,4],2))
print(array_convert([1,2,3,4],3))