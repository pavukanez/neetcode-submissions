class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for c in s:
            if c != ']':
                stack.append(c)
                continue
            
            temp = []
            while stack and stack[-1] != '[':
                temp.append(stack.pop())           
            stack.pop()

            curC = ""            
            while stack and stack[-1].isdigit():
                curC += stack.pop()
                
            temp.reverse()
            curS = "".join(temp)
            curC = int(curC[::-1])
            stack.append(curS * curC)

        return "".join(stack)