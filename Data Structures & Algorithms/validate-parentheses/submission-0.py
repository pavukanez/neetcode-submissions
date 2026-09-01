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
                top = stack.pop()
                if c != brackets.get(top):
                    return False
            else:
                stack.append(c)        
        return True