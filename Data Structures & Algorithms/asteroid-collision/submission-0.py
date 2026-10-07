class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for ast in asteroids:
            destroyed = False

            while stack and stack[-1] > 0 and ast < 0:
                if abs(stack[-1]) < abs(ast):
                    stack.pop()
                    continue
                elif abs(stack[-1]) == abs(ast):
                    destroyed = True
                    stack.pop()
                    break
                else:
                    destroyed = True
                    break
            
            if not destroyed:
                stack.append(ast)
        
        return stack