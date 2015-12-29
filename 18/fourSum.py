class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        size = len(nums)
        if size < 4 :
            return []

        nums.sort()
        rlist = []

        for i in range(size - 3):
            if i > 0 and nums[i] == nums[i-1]: continue
            for j in range(i+1,size-2):
                if j > (i + 1) and nums[j] == nums[j - 1]: continue
                t = target - nums[i] - nums[j]
                lo = j + 1;
                hi = (size - 1);
                while lo < hi:
                    sums = nums[lo] + nums[hi]
                    if sums < t :
                        lo += 1;
                    elif sums > t:
                        hi -= 1;
                    else :
                        rlist.append([nums[i],nums[j],nums[lo],nums[hi]])
                        while lo < hi and nums[lo] == nums[lo+1]: lo += 1
                        while lo < hi and nums[hi] == nums[hi-1]: hi -= 1
                        lo += 1
                        hi -= 1
        return rlist
