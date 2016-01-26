class Solution(object):
    def combinationSum(self, candidates, target):
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
        elif t < c[0]:
            return
        for i in c:
            if s and i < s[-1]: continue
            self.combinations(r,c,s+[i],t-i)
        return

if __name__ == '__main__':
    so = Solution()
    so.combinationSum([2,3,6,7],20)
