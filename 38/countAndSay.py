class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        i = 1
        s = '1'
        while i < n:
            s = self.say(s)
            i += 1
        
        return s
    
    def say(self,s):
        n = len(s)
        count = 0
        res = []
        for i in range(n):
            if count == 0:
                count += 1
            elif i>0 and s[i] == s[i-1]:
                count += 1
            else:
                res.append(str(count)+s[i-1])
                count = 1
        if count :
            res.append(str(count)+s[-1])
        return "".join(res)

if __name__ == "__main__":
    so = Solution()
    so.countAndSay(5)