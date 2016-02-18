class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 2:
            return nums[0]

        lo = 0
        hi = n - 1
        while lo < hi:
            if nums[lo] < nums[hi]: return nums[lo]

            mid = (lo + hi)/2
            if nums[mid] >= nums[lo]:
                lo = mid + 1
            else:
                hi = mid

        return nums[lo]
