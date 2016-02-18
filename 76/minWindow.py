"""1. Use two pointers: start and end to represent a window.
2. Move end to find a valid window.
3. When a valid window is found, move start to find a smaller window.
"""
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s or not t: return ""
        d = {}
        n = len(s)
        m = len(t)
        if n < m: return ""
        for i in t:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        
        start = 0
        end = 0
        count = m
        ans = n+1
        substr = ""
        
        while start < n-m+1 and end <= n:
            if count:
                if end != n:
                    if s[end] in d:
                        if d[s[end]] > 0:
                            count -= 1
                        d[s[end]] -= 1
                end += 1
            else :
                if ans > (end-start):
                    ans = end - start
                    substr = s[start:end]
                
                if s[start] in d:
                    d[s[start]] += 1
                    if d[s[start]] > 0:
                        count += 1
                start += 1
        if ans == n+1: return ""
        
        return substr