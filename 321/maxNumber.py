class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        n,m = len(nums1),len(nums2)
        ans = []

        for i in range(k+1):
            j = k - i
            if i > n or j > m: continue
            str1 = self.maxSingleStr(nums1,i)
            str2 = self.maxSingleStr(nums2,j)
            ans = max(ans,self.mergeStr(str1,str2))
        return ans

    @staticmethod
    def mergeStr(nums1,nums2):
        ret = []
        while nums1 or nums2:
            if nums1 > nums2:
                ret.append(nums1[0])
                nums1 = nums1[1:]
            else:
                ret.append(nums2[0])
                nums2 = nums2[1:]
        return ret

    @staticmethod
    def maxSingleStr(nums,part):
        n = len(nums)
        ret = [-1]
        if part > n: return nums

        while part > 0:
            start = ret[-1] + 1
            end = n - part + 1
            ret.append(max(range(start,end),key=nums.__getitem__))
            part -= 1

        ret = [nums[i] for i in ret[1:]]
        return ret
