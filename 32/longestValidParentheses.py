class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0
        ans = 0
        stack = []

        for letter in s:
            if letter == ')':
                if not stack:
                    stack.append(-1)
                elif stack[-1] == 0:
                    stack.pop()
                    if not stack or stack[-1] <= 0:
                        stack.append(2)
                    else:
                        stack[-1] = stack[-1] + 2
                elif stack[-1] == -1:
                    stack.append(-1)
                else:
                    count = stack.pop()
                    if not stack or stack[-1] != 0:
                        stack.append(count)
                        stack.append(-1)
                    else:
                        stack.pop()
                        count += 2
                        while stack and stack[-1]>0:
                            count += stack.pop()
                        stack.append(count)
            else:
                stack.append(0)

        ans = max(stack)
        ans = 0 if ans == -1 else ans
        return ans
                    
