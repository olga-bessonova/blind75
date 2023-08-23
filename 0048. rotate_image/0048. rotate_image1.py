# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. 
# DO NOT allocate another 2D matrix and do the rotation.

def rotate(matrix):
  l, r = 0, len(matrix[0]) - 1

  while l < r:
        for i in range(r-l):
            t, b = l, r # since it's a square matrix
            # store the top left cell
            top_left_cell = matrix[t][l+i]

            # update top left:
            matrix[t][l+i] = matrix[b-i][l]

            # update bottom left:
            matrix[b-i][l] = matrix[b][r-i]

            # update bottom right:
            matrix[b][r-i] = matrix[t+i][r]

            # update top right left:
            matrix[t +i][r] = top_left_cell
        l += 1
        r -= 1 
  return matrix

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(rotate(matrix))# Output: [[7,4,1],[8,5,2],[9,6,3]]