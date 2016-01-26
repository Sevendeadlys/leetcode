class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        nums = (2,3,4,5,6,7,8,9)
        letters = ('abc','def','ghi','jkl','mno','pqrs','tuv','wxyz')
        d = dict(zip(nums,letters))
        ret = []
        self.letters(ret,d,'',digits)
        print ret

    def letters(self,r,d,s,digits):
        if not digits:
            r.append(s)
            return
        b = int(digits[0])
        digits = digits[1:]

        if b in d:
            for ss in d[b]:
                self.letters(r,d,s+ss,digits)
        else:
            self.letters(r,d,s,digits)

if __name__ == '__main__':
    so = Solution()
    so.letterCombinations('123')
