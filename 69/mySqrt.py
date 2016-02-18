class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        num = 2
        while (num**2) < x:
            num <<= 1

        lo = num>>1
        hi = num

        while lo <= hi:
            mid = (lo+hi)/2
            midnum = mid**2
            if midnum < x:
                lo = mid + 1
            elif midnum > x:
                hi = mid - 1
            else :
                return mid

        return lo-1
