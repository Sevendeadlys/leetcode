class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        charmap = {}
        longest = 0
        m = 0

        for i in range(len(s)):
            if s[i] in charmap and m <= charmap[s[i]]:
                m = charmap[s[i]] + 1

            charmap[s[i]] = i
            longest = max(longest,i-m+1)

        return longest
