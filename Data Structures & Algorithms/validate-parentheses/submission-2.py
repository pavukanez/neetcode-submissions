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
                if len(stack) > 0:
                    top = stack.pop()
                else:
                    top = ''
                    
                if c != brackets.get(top):
                    return False
            else:
                stack.append(c)  
              
        return len(stack) == 0