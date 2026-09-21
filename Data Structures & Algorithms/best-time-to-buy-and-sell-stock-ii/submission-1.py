class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cache = {}
        
        def dfs(idx, bought):
            if idx == len(prices):
                return 0
            if (idx, bought) in cache:
                return cache[(idx, bought)]

            do_nothing = dfs(idx + 1, bought)
            if bought:
                res = max(do_nothing, prices[idx] + dfs(idx + 1, False))
            else:
                res = max(do_nothing, -prices[idx] + dfs(idx + 1, True))
            cache[(idx, bought)] = res
            return res

        return dfs(0, False)