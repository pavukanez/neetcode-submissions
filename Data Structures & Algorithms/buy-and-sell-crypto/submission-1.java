class Solution {
    public int maxProfit(int[] prices) {
        // assume we buy the first price
        int profit = 0, buy = prices[0];

        for (int i=1;i<prices.length;i++){
            // if current price is higher then buying price -> profit
            if (prices[i] > buy){
                profit = Math.max(profit, prices[i] - buy);
            }
            // found lower price then current assumed buying price -> update assume buying price to the lower price
            else {
                buy = prices[i];
            }
        }
        return profit;
    }
}
