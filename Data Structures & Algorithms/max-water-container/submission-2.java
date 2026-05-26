class Solution {
    public int maxArea(int[] heights) {
        int res = 0, l = 0, r = heights.length - 1;

        while (l < r){
            // calculate current amount of water between those bars
            int amount = Math.min(heights[l], heights[r]) * (r-l);
            res = Math.max(res, amount);

            // if left bar shorter -> move L to mid to maybe find taller bar
            if (heights[l] < heights[r]) l++;
            // else move right bar to mid
            else r--;
        }
        return res;
    }
}
