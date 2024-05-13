def setZeroes(matrix):
    nrows = len(matrix)
    ncols = len(matrix[0])
    first_element = False
    first_row = False # true if any cell of the 1st row == 0
    first_column = False # true if any cell of the 1st column == 0

    # update first_column
    for r in range(nrows):
        if matrix[r][0] == 0:
            first_column = True
    # update first_row
    for c in range(ncols):
        if matrix[0][c] == 0:
            first_row = True
    
    # update first_column
    for r in range(nrows):
        for c in range(ncols):
            if matrix[r][c] == 0:
                if r==0 and c==0:
                    first_element = True
                matrix[0][c] = 0
                
                if r > 0:
                    matrix[r][0] = 0                        
    # 2. A reduced matrix - a matrix w/o 1st row and column
    # go through a reduced matrix
    # print(matrix)
    for r in range(1,nrows):
        for c in range(1,ncols):
            if matrix[0][c] == 0 or matrix[r][0] == 0:
                matrix[r][c] = 0
    if first_element == True:
        for r in range(nrows):
            matrix[r][0] = 0
        for c in range(ncols):
            matrix[0][c] = 0
    
    if first_column == True:
        for r in range(nrows):
            matrix[r][0] = 0
    if first_row == True:
        for c in range(ncols):
            matrix[0][c] = 0
    return matrix


matrix = [[1,1,1],[1,0,1],[1,1,1]]
print(setZeroes(matrix)) #[[1,0,1],[0,0,0],[1,0,1]]

matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
print(setZeroes(matrix)) #[[0,0,0,0],[0,4,5,0],[0,3,1,0]]

    

           
            
            

