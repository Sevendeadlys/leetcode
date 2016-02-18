class Solution1(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]: return False

        m = len(matrix)
        n = len(matrix[0])

        i = 0
        while i < m:
            """
            Binary search every list
            """
            if target in matrix[i]:
                return True
            i += 1

        return False

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]: return False

        m = len(matrix)
        n = len(matrix[0])

        r = 0
        c = n - 1

        while r < m and c >= 0:
            if target == matrix[r][c]:
                return True
            elif target > matrix[r][c]:
                r += 1
            else :
                c -= 1

        return False
