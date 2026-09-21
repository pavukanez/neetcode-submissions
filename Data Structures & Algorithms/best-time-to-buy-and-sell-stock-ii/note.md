# Problem statement

You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. However, you can buy it then immediately sell it on the same day. Also, you are allowed to perform any number of transactions but can hold at most one share of the stock at any time.

Find and return the maximum profit you can achieve.

Example 1:

Input: prices = [7,1,5,3,6,4]

Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4. Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3. Total profit is 4 + 3 = 7.

Example 2:

Input: prices = [1,2,3,4,5]

Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4. Total profit is 4.

Constraints:

1 <= prices.length <= 30,000

0 <= prices[i] <= 10,000


# Brute force

- create a dfs function using current idx, bought condition (True if holding stock, False if not):
    - if processed all days -> return 0
    - 2 options:
        - if not holding stock: skip today VS (sell today stock, tomorrow no stock)
        - else: skip today VS (buy today stock, tomorrow have stock)
    - return res
- return dfs(0, False) as it is index 0, not holding stock
    
```
def maxProfit(self, prices: List[int]) -> int:
    
    def dfs(idx, bought):
        if idx == len(prices):
            return 0

        do_nothing = dfs(idx + 1, bought)
        if bought:
            res = max(do_nothing, prices[idx] + dfs(idx + 1, False))
        else:
            res = max(do_nothing, -prices[idx] + dfs(idx + 1, True))
        return res

    return dfs(0, False)
```

TC: O(2^n)

SC: O(n)

# DP (Top-Down)
Brute forcing cause TLE as there were many repeated steps -> create a 2D hashmap for memoization of maximum profit at ith day with buy/sell status (i, bought)


```
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
```

TC: O(n)

SC: O(n)

# DP (Bottom-Up)
Iterate backwards from end, 2 choices:
- dont current have stock -> skip today VS (buy stock today + tomorrow have stock)
- currently have stock -> skip today VS (sell stock today + tomorrow no stock)

return dp[0][0] no profit, no stock

```
def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0] * 2 for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            dp[i][0] = max(dp[i + 1][0], -prices[i] + dp[i + 1][1])
            dp[i][1] = max(dp[i + 1][1], prices[i] + dp[i + 1][0])

        return dp[0][0]
```

TC: O(n)

SC: O(n)

# DP (Bottom-Up) (Space Optimized)
Technically if at ith then only needs data at (i+1)th -> use next_buy, next_sell, cur_buy, cur_sell

```
def maxProfit(self, prices: List[int]) -> int:
    n = len(prices)
    cur_buy = cur_sell = 0
    next_buy = next_sell = 0

    for i in range(n - 1, -1, -1):
        cur_buy = max(next_buy, -prices[i] + next_sell)
        cur_sell = max(next_sell, prices[i] + next_buy)
        next_buy = cur_buy
        next_sell = cur_sell
    
    return cur_buy
```

TC: O(n)

SC: O(1)