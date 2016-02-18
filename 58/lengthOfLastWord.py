class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        if not s: return 0

        index = s.rfind(' ')
        if index == -1:
            return len(s)
        else:
            return len(s) - index - 1
