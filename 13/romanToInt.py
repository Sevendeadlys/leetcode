class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        values = (1000,900,500,400,100,90,50,40,10,9,5,4,1)
        keys = ("M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I")
        d = dict(zip(keys,values))
        ret = 0
        while len(s):
            v = s[:2]
            if v in d:
                s = s[2:]
                ret = ret + d[v]
            else:
                v = s[:1]
                s = s[1:]
                ret = ret + d[v]
        return ret
