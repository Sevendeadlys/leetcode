class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ret = []
        candidates.sort()
        self.combinations(ret,candidates,[],target)
        return ret

    def combinations(self,r,c,s,t):
        if t == 0:
            r.append(s)
            return
        elif not c or t < c[0]:
            return
        for i,val in enumerate(c):
            if i > 0 and len(c) > 1 and c[i] == c[i-1]:continue
            self.combinations(r,c[i+1:],s+[val],t-val)
        return

if __name__ == '__main__':
    so = Solution()
    so.combinationSum2([1,1],1)
