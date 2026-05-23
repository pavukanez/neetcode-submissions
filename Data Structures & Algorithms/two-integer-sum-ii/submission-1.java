class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int l = 0, r = numbers.length - 1;

        while(l < r){
            int sum = numbers[l] + numbers[r];
            // if current sum greater than target -> move right to mid
            if (sum > target){
                r--;
            }
            // elif current sum less than target -> move left to mid
            else if (sum < target){
                l++;
            }
            // else sum equals target -> return those indexes + 1
            else return new int[]{l+1, r+1};
        }
        return new int[0];
    }
}
