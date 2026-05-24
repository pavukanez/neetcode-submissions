class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);

        List<List<Integer>> res = new ArrayList<>();
        for(int i=0;i<nums.length;i++){
            // skip processed targets
            if (i>0 && nums[i] == nums[i-1]) continue;

            // if target is greater than 0 -> impossible for all 3 positive numbers afterwards to add up to 0
            if (nums[i] > 0) break;

            // 2sum with sorted list
            int target = -nums[i];
            int l = i + 1, r = nums.length - 1;
            while (l < r){
                int sum = nums[l] + nums[r];
                if (sum < target) l++;
                else if (sum > target) r--;
                else {
                    res.add(new ArrayList<>(Arrays.asList(nums[l], nums[r], nums[i])));

                    // there are more potentials pairs that add up to target
                    // but must not be duplicate as the pair we just found
                    // move L to mid until next number not equals to cur
                    while (l < r && nums[l] == nums[l+1]) l++;

                    // move R to mid until next number not equals to cur
                    while (r > l && nums[r] == nums[r-1]) r--;

                    // move L and R to the next distinct num
                    l++;
                    r--;
                }
            }
        }
        return res;
    }
}
