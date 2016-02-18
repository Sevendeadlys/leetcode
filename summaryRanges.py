class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        res = []
        if not nums: return res
        start = nums[0]
        end = nums[0]
        for num in nums[1:]:
            if num == end + 1:
                end = num
            else:
                if start == end:
                    res.append(str(start))
                else:
                    res.append(str(start)+'->'+str(end))

                start = num
                end = num
        if start==end:
            res.append(str(start))
        else:
            res.append(str(start)+'->'+str(end))
        return res
