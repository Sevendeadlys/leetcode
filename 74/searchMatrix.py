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

        lo = 0
        hi = m*n - 1

        while lo <= hi:
            mid = (lo + hi)/2
            i = mid // n
            j = mid % n

            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                lo = mid + 1
            else:
                hi = mid - 1

        return False
