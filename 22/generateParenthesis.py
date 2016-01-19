class Solution(object):
    def generate(self,r,n,s):
        size = len(s)
        maxSize = 2*n
        if size == maxSize and s.count('(') == n:
            r.append(s)
        elif size < maxSize:
            if s.count('(') < ( size/2 if size%2 == 0 else size/2+1):
                return
            else:
                self.generate(r,n,s+'(')
                self.generate(r,n,s+')')
        else:
            return

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        rlist = []
        self.generate(rlist,n,"")
        return rlist
