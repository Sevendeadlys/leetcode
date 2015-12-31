class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        wordDic = {}

        if pattern == '' or str == '':
            return False
        words = str.split(' ')
        size = len(pattern)
        wordSize = len(words)

        if size != wordSize :
            return False

        if len(set(pattern)) != len(set(words)):
            return False

        for i in range(size):
            if pattern[i] not in wordDic:
                wordDic[pattern[i]] = words[i]
            else :
                word = wordDic[pattern[i]]
                if word != words[i]:
                    return False

        return True
