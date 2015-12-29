class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums_len = len(nums)
        if nums_len<3:
            return MAXINT

        nums.sort()
        min_diff = abs(nums[0] + nums[1] + nums[2] - target)
        ret = nums[0] + nums[1] + nums[2]
        for i in range(nums_len-2):
            if i > 0 and nums[i] == nums[i-1]: continue
            low = i + 1;
            high = nums_len - 1;
            while(low < high):
                sum_num = nums[low] + nums[high] + nums[i]
                diff = sum_num - target

                if diff > 0:
                    while low<high and nums[high] == nums[high-1]: high -= 1
                    high -= 1
                elif diff < 0:
                    while low<high and nums[low] == nums[low+1]: low += 1
                    low += 1
                else :
                    return target

                if min_diff > abs(diff):
                    min_diff = abs(diff)
                    ret = sum_num
        return ret
