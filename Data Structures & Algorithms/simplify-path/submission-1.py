class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        count = 0
        for c in path:
            if not stack or c.isalnum() or c == '.' or c == '_':
                stack.append(c)
                continue
            
            # c is '/'
            cur = ""
            while stack and stack[-1] != '/':
                cur += stack.pop()
            cur = cur[::-1]
            
            if cur == '.' or cur == '':
                continue
            elif cur == '..':
                stack.pop()
                while stack and stack[-1] != '/':
                    stack.pop()
            else:
                for c in cur:
                    stack.append(c)
                stack.append('/')
        
        if len(stack) <= 1:
            return "/"

        return "".join(stack) if stack[-1] != '/' else "".join(stack[:-1])


