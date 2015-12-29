"""
1. use a dict to store the num and index
2. search the array, find (target - num) in dict
time O(n)
"""
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        
        for i,num in enumerate(nums):
            if target-num in d:
                return d[target-num]+1,i+1
            
            d[num] = i
        return -1,-1