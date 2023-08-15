# Given an m x n matrix, return all elements of the matrix in spiral order.
def spiralOrder(matrix):
    # 1 2 3
    # 4 5 6
    # 7 8 9

    # result [1,2,3,6,9,8,7,4,5]
    # [0,0] -> [0,ncol] same row but column vary
    # [0+1,ncol] -> [bottom,ncol] row vary same column
    # [nrow, 0] <- [nrow, ncol]
    # [nrow-1, 0] -> [0+1,0]
    # [0+1,0+1] -> [0+1, ncol-1]
    res = []
    l, r = 0, len(matrix[0]) #r=3
    t, b = 0, len(matrix)
    # matrix = [1,2,3] l,r = 0, 3   t,b = 0, 1 

    while l < r and t < b:
        # top row
        for i in range(l, r):
            res.append(matrix[l][i])
        t += 1


        # right column
        for i in range(t, b):
            res.append(matrix[i][r-1])
        r -=1 #r=2
        
        if len(res) == len(matrix[0]) * len(matrix):
            break

        # bottom row
        for i in reversed(range(l, r)): 
            res.append(matrix[b-1][i]) 
        b -= 1

        # left column
        for i in reversed(range(t, b)):
            res.append(matrix[i][l])
        l +=1 #r=2
    return res

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(spiralOrder(matrix))


