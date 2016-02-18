class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or not words or not words[0]:
            return []
        
        size = len(words[0])
        n = len(s)
        m = size*len(words)
        if n < m: return []
        
        rlist = []
        d = {}
        for word in words:
            if word in d:
                d[word] += 1
            else:
                d[word] = 1
        
        for i in range(n):
            if (n-i) < m : return rlist
            subd = {}
            for j in range(i,i+m,size):
                tword = s[j:j+size]
                if tword not in d:
                    break
                else:
                    if tword in subd:
                        subd[tword] += 1
                    else:
                        subd[tword] = 1
            if subd == d: rlist.append(i)
        return rlist
                    