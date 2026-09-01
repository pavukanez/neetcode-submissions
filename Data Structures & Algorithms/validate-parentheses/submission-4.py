class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        brackets = {
            '[': ']',
            '{': '}',
            '(': ')'
        }

        for c in s:
            if c not in brackets:
                if stack and c == brackets[stack.pop()]:
                    continue
                else:
                    return False
            else:
                stack.append(c)  
              
        return len(stack) == 0