class Solution {
    public int maxArea(int[] heights) {
        int res = , l = 0, r = heights.length - 1;
        while (l < r){
            int amount = Math.min(heights[l], heights[r]) * (r-l);
            res = Math.max(res, amount);

            if (heights[l] < heights[r]) l++;
            else r--;
        }
        return res;
    }
}
