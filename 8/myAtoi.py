"""
Be careful with the boundary of 32-bit value
"""
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        import re
        pattern = re.compile('([+-]?\d+)', re.I)

        m = pattern.match(str.strip())
        if m:
            tmp = int(m.group(1))
            if tmp > 2147483647:
                return 2147483647
            elif tmp < -2147483648:
                return -2147483648
            else:
                return tmp
        else:
            return 0
