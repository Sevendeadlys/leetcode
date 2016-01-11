class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        import math
        
        maxIntThree = pow(3,math.floor(math.log(0x7fffffff)/math.log(3)))
        return n>0 and (maxIntThree%n)==0