class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n < 2: return
        pos = n - 1
        
        while pos > 0 and nums[pos] <= nums[pos-1]: pos -= 1
        
        if not pos:
            return nums[::-1]
        
        i = n - 1
        
        while i >= pos and nums[i] <= nums[pos-1]: i -= 1
        
        nums[i], nums[pos-1] = nums[pos-1],nums[i]
        temp = nums[pos:]
        return nums[0:pos] + temp[::-1]
        

if __name__ == "__main__":
    so = Solution()
    print so.nextPermutation([1,3,2])
