class Solution(object):
    def addBinary(self, a, b):
        l1,l2 = map(int,a), map(int,b)
        res, carry= [], 0
        
        while l1 or l2:
            num = carry
            if l1:
                num += l1[-1]
                l1.pop()
            
            if l2:
                num += l2[-1]
                l2.pop()
            carry = num/2
            num %= 2
            res.append(num)
        if carry:
            res.append(carry)
        return "".join([str(i) for i in res[::-1]])

if __name__ == "__main__":
    so = Solution()
    print so.addBinary('1010', '1011')