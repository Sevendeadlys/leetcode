class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        if n == 0: return -1
        m = self.findMin(nums)

        lo = 0
        hi = n - 1
        while lo <= hi:
            mid = (lo+hi)/2
            realmid = (mid+m)%n
            if nums[realmid] == target:
                return realmid
            elif nums[realmid] > target:
                hi = mid - 1
            else:
                lo = mid + 1

        return -1

    def findMin(self, nums):
        lo = 0
        hi = len(nums) - 1
        while lo < hi:
            if nums[lo] < nums[hi]: return lo

            mid = (lo + hi)/2
            if nums[mid] >= nums[lo]:
                lo = mid + 1
            else:
                hi = mid
        return lo
