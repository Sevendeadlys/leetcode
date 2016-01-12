'''
To create the max number from num1 and nums2 with k elements,
we assume the final result combined by i numbers (denotes as left)
from num1 and j numbers (denotes as right) from nums2, where i+j==k.

Obviously, left and right must be the maximum possible number in num1 and num2 respectively.
i.e. num1 = [6,5,7,1] and i == 2, then left must be [7,1].

The final result is the maximum possible merge of all left and right.

So there're 3 steps:
    iterate i from 0 to k.
    find max number from num1, num2 by select i , k-i numbers, denotes as left, right
    find max merge of left, right
function maxSingleNumber select i elements from num1 that is maximum.
The idea find the max number one by one. i.e. assume nums [6,5,7,1,4,2], selects = 3.
1st digit: find max digit in [6,5,7,1], the last two digits [4, 2] can not be selected at this moment.
2nd digits: find max digit in [1,4], since we have already selects 7, we should consider elements after it,
also, we should leave one element out. 3rd digits: only one left [2], we select it. and function output [7,4,2]
function mergeMax find the maximum combination of left, and right.
'''
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
