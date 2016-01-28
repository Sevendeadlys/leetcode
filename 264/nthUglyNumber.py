"""
We have an array k of first n ugly number. We only know, at the beginning, the first one, which is 1. Then

k[1] = min( k[0]x2, k[0]x3, k[0]x5). The answer is k[0]x2. So we move 2's pointer to 1. Then we test:

k[2] = min( k[1]x2, k[0]x3, k[0]x5). And so on. Be careful about the cases such as 6, in which we need to forward both pointers of 2 and 3.

x here is multiplication.
"""
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1: return 1;
        """
        val = 2
        while len(stack) < n:
            num = val
            flag = True
            while flag and num != 1:
                if not num%2:
                    num /= 2
                elif not num%3:
                    num /= 3
                elif not num%5:
                    num /= 5
                else:
                    flag = False
            if flag:
                stack.append(val)
            val += 1

        return stack[-1]
        """
        dp = [0]*n
        dp[0] = 1
        t2, t3, t5 = 0, 0, 0
        for i in range(1,n):
            dp[i] = min(dp[t2]*2,dp[t3]*3,dp[t5]*5)
            if dp[i] == dp[t2]*2: t2 += 1
            if dp[i] == dp[t3]*3: t3 += 1
            if dp[i] == dp[t5]*5: t5 += 1

        return dp[-1]
