class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        n = len(nums)
        res.append(nums)
        if len(nums) < 2: return res
        
        temp = self.next_permute(nums,n)
        while temp != nums:
            res.append(temp)
            temp = self.next_permute(temp,n)
        return res
    
    def next_permute(self,nums,n):
        new = nums[:]
        pos = n - 1
        while pos > 0 and new[pos] <= new[pos-1]: pos -= 1
        if not pos:return new[::-1]
        
        i = n - 1
        while i >= pos and new[i] <= new[pos-1]: i -= 1
        
        new[i], new[pos-1] = new[pos-1],new[i]
        end = n - 1
        while pos < end:
            new[pos],new[end] = new[end],new[pos]
            pos += 1
            end -= 1
        return new