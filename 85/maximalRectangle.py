class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        height = [-1,-1]
        width = [-1,-1]
        for i in range(len(matrix)):
            if '1' in matrix[i]:
                height[1] = i
                if height[0] == -1:
                    height = i
            
            for j in range(len(matrix[0])):
                if matrix[i][j] == '1':
                    width[1] = max(j,width[1])
                    width[0] = j if width[0]==-1 else min(j,width[0])
        
        if -1 in height or -1 in width:
            return 0
        
        return (height[1] - height[0] + 1)*(width[1] - width[0] + 1)