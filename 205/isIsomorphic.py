class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s == '' and t == '':
            return True

        return (len(set(zip(s,t))) == len(set(s)) == len(set(t)) and len(s) == len(t))
