# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        return self.isValid(root,-(1<<32),(1<<32))

    def isValid(self,root,small,large):
        if not root:
            return True

        if root.val > small and root.val < large:
            return self.isValid(root.left,small,root.val) and self.isValid(root.right,root.val,large)
        else:
            return False
