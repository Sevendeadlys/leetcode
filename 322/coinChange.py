class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0: return 0
        coins.sort(reverse=True)
        dp = [-1]*(amount+1)
        for i in range(1,amount+1):
            if i in coins:
                dp[i] = 1
            else:
                ans = -1
                for j in coins:
                    if i <= j or dp[i-j] == -1:
                        continue
                    else:
                        ans = dp[i-j]+1 if ans == -1 else min(ans, dp[i-j]+1)
                dp[i] = ans
        return dp[amount]
