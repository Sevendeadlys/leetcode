"""
the maxint value shall be considered
"""
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = str(x)
        lo = 0
        hi = len(s) - 1
        ret = ''

        if s[0] in '+-':
            lo += 1
            ret += s[0]

        while hi >= lo:
            ret += s[hi]
            hi -= 1
        ret = int(ret)
        if abs(ret) > 2147483647:
            return 0
        return ret
