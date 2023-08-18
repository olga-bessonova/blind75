# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        nrows = len(matrix)
        ncols = len(matrix[0])
        if matrix[0][0] == 0:
            first_element = True
        else:
            first_element = False

        print('first element', first_element)
        first_row = False # true if any cell of the 1st row == 0
        first_column = False # true if any cell of the 1st column == 0
        # 1. go through all cells, find 0 and update 1st row, 1st column w/o 1st cell [0,0]
        # update first_column
        for r in range(nrows):
            if matrix[r][0] == 0:
                first_column = True
        # update first_row
        for c in range(ncols):
            if matrix[0][c] == 0:
                first_row = True
        print('first element', first_element)
        # update first_column
        for r in range(nrows):
            for c in range(ncols):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0                        
                    else:
                        first_element = True
                        
                   

                    
        print('first element', first_element)
        print('1',matrix)
        # 2. A reduced matrix - a matrix w/o 1st row and column
        # go through a reduced matrix
        
        for r in range(1,nrows):
            for c in range(1,ncols):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
        print('2 ',matrix)
        print('first element', first_element)
        if first_element == True:
            for r in range(nrows):
                matrix[r][0] = 0
            for c in range(ncols):
                matrix[0][c] = 0
        print('3 ',matrix)
        
        if first_column == True:
            for r in range(nrows):
                matrix[r][0] = 0
        print('4 ',matrix)
        if first_row == True:
            for c in range(ncols):
                matrix[0][c] = 0
        print('5 ',matrix)


    

           
            
            

