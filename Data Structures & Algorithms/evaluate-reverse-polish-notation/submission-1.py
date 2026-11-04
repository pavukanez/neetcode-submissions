class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {"+", "-", "*", "/"}

        for s in tokens:
            if s in operators:
                a = int(stack.pop())
                b = int(stack.pop())
                if s == "+":
                    res = b + a
                elif s == "-":
                    res = b - a
                elif s == "*":
                    res = b * a
                else:
                    res = b // a

                stack.append(res)
            else:
                stack.append(s)
                
        return stack[-1]
