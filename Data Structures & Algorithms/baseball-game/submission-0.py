class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for op in operations:
            if op == '+':
                b = stack.pop()
                a = stack.pop()
                c = a + b
                stack.append(a)
                stack.append(b)
                stack.append(c)
            elif op == 'D':
                stack.append(stack[-1] * 2)
            elif op == 'C':
                stack.pop()
            else:
                stack.append(int(op))
        
        return sum(stack)
