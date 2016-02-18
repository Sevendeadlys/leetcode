class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        start = 0
        end = 0
        n = len(nums)
        
        ans = n+1
        count = 0
        
        while start < n and end <= n:
            if count < s:
                if end != n:
                    count += nums[end]
                end += 1
            else :
                if ans > end - start:
                    ans = end - start
                count -= nums[start]
                start += 1
        
        if ans == n+1: return 0
        
        return ans