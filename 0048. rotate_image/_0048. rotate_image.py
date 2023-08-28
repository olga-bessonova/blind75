# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. 
# DO NOT allocate another 2D matrix and do the rotation.

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l, r = 0, len(matrix) - 1

        while l < r:
            for i in range(0, r-l):
                t, b = l, r
                # print('i = ',i)
                t_l_cell = matrix[t+i][l]
                # print(t_l_cell) 
                matrix[t+i][l] = matrix[b][l+i]
                matrix[b][l+i] = matrix[b-i][r]
                matrix[b-i][r] = matrix[t][r-i]
                matrix[t][r-i] = t_l_cell
                print(matrix)

            l += 1
            r -= 1
            


# def rotate(matrix):
  

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(rotate(matrix))# Output: [[7,4,1],[8,5,2],[9,6,3]]