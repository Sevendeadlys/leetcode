import time

class Solution1(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        ma = [["."]*n for _ in range(n)]
        rlist = []
        
        self.solveN(rlist,ma,n,0)
        return rlist
    
    def solveN(self,rlist,ma,n,i):
        if i == n:
            temp = []
            for t in range(n):
                temp.append("".join(ma[t]))
            rlist.append(temp)
            return
        for j in range(n):
            if self.checkQueen(ma,n,i,j):
                ma[i][j] = "Q"
                self.solveN(rlist,ma,n,i+1)
                ma[i][j] = "."
    
    def checkQueen(self,ma,n,i,j):
        for t in range(n):
            if "Q" == ma[t][j]:
                return False
        r = i - 1
        c = j - 1
        while r>=0 and c>=0:
            if "Q" == ma[r][c]:
                return False
            r -= 1
            c -= 1
        
        r = i - 1
        c = j + 1
        while r>=0 and c<n:
            if "Q" == ma[r][c]:
                return False
            r -= 1
            c += 1
        return True        

class Solution2(object):
    def solveNQueens(self, n):
        flag_col = [1]*n
        flag_45 = [1]*(2*n-1)
        flag_135 = [1]*(2*n-1)
        ma = [["."]*n for _ in range(n)]
        rlist = []
        self.solveN(rlist, ma, n, 0, flag_col, flag_45, flag_135)
        return rlist
    
    def solveN(self,rlist,ma,n,row,flag_col,flag_45,flag_135):
        if row == n:
            temp = []
            for t in range(n):
                temp.append("".join(ma[t]))
            rlist.append(temp)
        
        for col in range(n):
            if flag_col[col] and flag_45[row+col] and flag_135[n-1+row-col]:
                flag_col[col] = 0
                flag_45[row+col] = 0
                flag_135[n-1+row-col] = 0
                ma[row][col] = "Q"
                self.solveN(rlist, ma, n, row+1, flag_col, flag_45, flag_135)
                flag_col[col] = 1
                flag_45[row+col] = 1
                flag_135[n-1+row-col] = 1
                ma[row][col] = "."                
        

if __name__ == "__main__":
    so = Solution2()
    tick = time.time()
    so.solveNQueens(9)
    tick = time.time() - tick
    print tick