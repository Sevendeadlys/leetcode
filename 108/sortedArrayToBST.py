# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums: return None
        return self.helper(nums,0,len(nums)-1)
    
    def helper(self,nums,lo,hi):
        if hi < lo : return None
        mid = (hi + lo)/2
        node = TreeNode(nums[mid])
        node.left = self.helper(nums,lo,mid-1)
        node.right = self.helper(nums,mid+1,hi)
        return node

if __name__ == "__main__":
    so = Solution()
    so.sortedArrayToBST([1,2,3,4,5,6,7,8,9])