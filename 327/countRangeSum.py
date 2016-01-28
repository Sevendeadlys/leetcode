class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        if not nums: return 0
        n = len(nums)
        sums = []
        sums.append(0)
        for i in range(n):
            sums.append(sums[i] + nums[i])
        asn = 0
        for i in range(n):
            for j in range(i+1,n+1):
                if lower<= sums[j] - sums[i] <= upper:
                    asn += 1
        return asn
