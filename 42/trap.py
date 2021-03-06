"""Here is my idea: instead of calculating area by height*width, we can think it in a cumulative way.
In other words, sum water amount of each bin(width=1).
Search from left to right and maintain a max height of left and right separately,
which is like a one-side wall of partial container.
Fix the higher one and flow water from the lower part.
For example, if current height of left is lower,
we fill water in the left bin. Until left meets right, we filled the whole container.
"""
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right, maxleft, maxright = 0, len(height)-1, 0, 0
        res = 0

        while left <= right:
            if height[left] <= height[right]:
                if height[left] >= maxleft:
                    maxleft = height[left]
                else:
                    res += maxleft - height[left]
                left += 1
            else:
                if height[right] >= maxright:
                    maxright = height[right]
                else:
                    res += maxright - height[right]
                right -= 1
        return res
