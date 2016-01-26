class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row = [[0] * 9 for _ in range(9)]
        col = [[0] * 9 for _ in range(9)]
        block = [[0] * 9 for _ in range(9)]
        
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.': continue
                
                if board[i][j] in row[i] or board[i][j] in col[j] or board[i][j] in block[(i//3)*3 + j//3]:
                    return False
                else:
                    row[i][j] = board[i][j]
                    col[j][i] = board[i][j]
                    block[(i//3)*3 + j//3][(i%3)*3+j%3] = board[i][j]
        
        return True