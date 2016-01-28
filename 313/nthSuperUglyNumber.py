class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        from sys import maxint
        while 1 in primes: primes.remove(1)
        if n == 1: return 1
        if not primes: return 0
        plen = len(primes)
        count = [0]*plen
        dp = [0]*n
        dp[0] = 1

        for i in range(1,n):
            ans = primes[0]*dp[count[0]]
            for j in range(1,plen):
                if ans >= primes[j]*dp[count[j]]:
                    ans = primes[j]*dp[count[j]]
            for index in range(plen):
                if ans == primes[index]*dp[count[index]]:
                    count[index] = count[index] + 1
            dp[i] = ans
        return dp[-1]
