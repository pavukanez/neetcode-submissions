class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {"+", "-", "*", "/"}

        for s in tokens:
            if s in operators:
                a = stack.pop()
                b = stack.pop()
                if s == "+":
                    res = b + a
                elif s == "-":
                    res = b - a
                elif s == "*":
                    res = b * a
                else:
                    res = int(b / a)

                stack.append(res)
            else:
                stack.append(int(s))
                
        return stack[-1]