class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(open, close, cur):
            if open < close or open > n or close > n:
                return
            
            if open == n and close == n:
                res.append(cur)
                return
            
            dfs(open + 1, close, cur + "(")
            dfs(open, close + 1, cur + ")")
        
        dfs(0, 0, "")

        return res


            