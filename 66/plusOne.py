class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1
        bit = len(digits) - 1
        res = []
        
        while carry and bit >= 0:
            val = carry + digits[bit]
            bit -= 1
            carry = val/10
            res.append(val%10)
        
        if carry:
            res.append(carry)
        else:
            while bit >= 0:
                res.append(digits[bit])
                bit -= 1
        return res[::-1]