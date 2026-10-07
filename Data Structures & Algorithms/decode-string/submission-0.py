class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for c in s:
            if c != ']':
                stack.append(c)
                continue
            
            curS = ""
            while stack and stack[-1] != '[':
                curS += stack.pop()           
            stack.pop()

            curC = ""            
            while stack and stack[-1].isdigit():
                curC += stack.pop()
                
            curS = curS[::-1]
            curC = int(curC[::-1])
            stack.append(curS * curC)

        return "".join(stack)