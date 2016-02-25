class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        res = [0]*(len(num1)+len(num2))
        
        for i,e1 in enumerate(reversed(num1)):
            for j,e2 in enumerate(reversed(num2)):
                res[i+j] += int(e1)*int(e2)
                res[i+j+1] += res[i+j]//10
                res[i+j] %= 10
        while len(res) > 1 and not res[-1]: res.pop()
        return "".join([str(i) for i in res[::-1]])