"""
The idea is to sort an input array and then run through
all indices of a possible first element of a triplet.
For each possible first element we make a standard
bi-directional 2Sum sweep of the remaining part of the array.
Also we want to skip equal elements to avoid duplicates in the answer
without making a set or smth like that.
"""
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        rlist = []
        if len(nums) < 3:
            return []

        nums.sort()

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]: continue
            target = -nums[i]
            if target < 0 :
                return rlist
            low = i + 1;
            high = len(nums) - 1
            while low < high:
                sum_num = nums[low] + nums[high]
                if sum_num < target:
                    low = low + 1
                elif sum_num > target:
                    high = high - 1
                else :
                    rlist.append([nums[i],nums[low],nums[high]])
                    while low < high and nums[low] == nums[low+1]: low += 1
                    while low < high and nums[high] == nums[high-1]: high -= 1
                    low += 1
                    high -= 1

        return rlist
