"""Be Naive First

When I first get this problem, it is far from dynamic programming to me. I started with the most naive idea the backtracking.

We have n balloons to burst, which mean we have n steps in the game. In the i th step we have n-i balloons to burst, i = 0~n-1.
Therefore we are looking at an algorithm of O(n!). Well, it is slow, probably works for n < 12 only.

Of course this is not the point to implement it. We need to identify the redundant works we did in it and try to optimize.

Well, we can find that for any balloons left the maxCoins does not depends on the balloons already bursted.
This indicate that we can use memorization (top down) or dynamic programming (bottom up) for all the cases
from small numbers of balloon until n balloons. How many cases are there? For k balloons there are C(n, k)
cases and for each case it need to scan the k balloons to compare. The sum is quite big still.
It is better than O(n!) but worse than O(2^n).

Better idea

We then think can we apply the divide and conquer technique?
After all there seems to be many self similar sub problems from the previous analysis.

Well, the nature way to divide the problem is burst one balloon and separate the balloons
into 2 sub sections one on the left and one one the right. However, in this problem
the left and right become adjacent and have effects on the maxCoins in the future.

Then another interesting idea come up. Which is quite often seen in dp problem analysis.
That is reverse thinking. Like I said the coins you get for a balloon does not depend on
the balloons already burst. Therefore instead of divide the problem by the first balloon
to burst, we divide the problem by the last balloon to burst.

Why is that? Because only the first and last balloons we are sure of their adjacent balloons before hand!

For the first we have nums[i-1]*nums[i]*nums[i+1] for the last we have nums[-1]*nums[i]*nums[n].

OK. Think about n balloons if i is the last one to burst, what now?

We can see that the balloons is again separated into 2 sections. But this time since
the balloon i is the last balloon of all to burst, the left and right section now
has well defined boundary and do not affect each other! Therefore we can do either
recursive method with memoization or dp.

Final

Here comes the final solutions. Note that we put 2 balloons with 1 as boundaries and
also burst all the zero balloons in the first round since they won't give any coins.
The algorithm runs in O(n^3) which can be easily seen from the 3 loops in dp solution.
"""
class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        nums = [1] + nums[:] + [1]
        n = len(nums)
        dp = [[0]*n for _ in range(n)]

        return self.burst(dp, nums, 0, n-1)

    def burst(self, dp, nums, left, right):
        if left+1 == right: return 0
        if dp[left][right] != 0 : return dp[left][right]

        ans = 0
        for i in range(left+1,right):
            ans = max(ans, nums[left]*nums[i]*nums[right]+\
                      self.burst(dp,nums,left,i)+\
                      self.burst(dp,nums,i,right))
        dp[left][right] = ans
        return ans

class Solution2(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        nums = [1] + nums[:] + [1]
        n = len(nums)
        dp = [[0]*n for _ in range(n)]

        for k in range(2,n):
            for left in range(0,n-k):
                right = left + k
                for i in range(left+1,right):
                    dp[left][right] = max(dp[left][right],\
                                      nums[left]*nums[i]*nums[right]+dp[left][i]+dp[i][right])

        return dp[0][n-1]
