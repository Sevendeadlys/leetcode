class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        left = ['(','[','{']
        right = [')',']','}']
        for letter in s:
            if letter in left:
                stack.append(letter)
            elif letter in right:
                i = right.index(letter)
                if not stack:
                    return False
                t = stack.pop()
                if t != left[i]:
                    return False
            else:
                return False
        return stack == []
