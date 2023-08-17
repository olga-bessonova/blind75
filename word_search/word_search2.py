# Given an m x n grid of characters board and a string word, return true if word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cells, 
# where adjacent cells are horizontally or vertically neighboring. 
# The same letter cell may not be used more than once.

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        nrows = len(board)
        ncols = len(board[0])
        path = set()

        def dfs(r, c, i):
            if i == len(word):
              return True
            if (r < 0 or c < 0 or 
                r >= nrows or c >= ncols or
                word[i] != board[r][c] or
                (r,c) in path):
              return False
            path.add((r,c))
            res = (dfs(r+1, c, i+1) or
                   dfs(r-1, c, i+1) or
                   dfs(r, c+1, i+1) or
                   dfs(r, c-1, i+1))
            path.remove((r,c))
            return res
        for r in range(nrows):
           for c in range(ncols):
              if dfs(r,c,0):
                 return True
        return False