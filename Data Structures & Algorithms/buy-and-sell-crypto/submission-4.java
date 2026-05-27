class Solution {
    public int maxProfit(int[] prices) {
        int profit = 0, l = 0, r = 1;

        while (r < prices.length){
            // buying price < selling price -> profit
            if (prices[l] < prices[r]){
                profit = Math.max(profit, prices[r] - prices[l]);
            }
            // buying price >= selling price -> found lower buying price
            else {
                l = r;
            }
            // move r to mid regardless
            r++;
            
        }
        return profit;
    }
}
