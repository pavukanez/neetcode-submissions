class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);

        List<List<Integer>> res = new ArrayList<>();
        for(int i=0;i<nums.length;i++){
            if ((i>0 && nums[i] == nums[i-1]) || nums[i] > 0) continue;

            int target = -nums[i];
            int l = i, r = nums.length - 1;
            while (l < r){
                if (nums[l] + nums[r] < target) l++;
                else if (nums[l] + nums[r] > target) r--;
                else {
                    List<Integer> cur = new ArrayList<>(Arrays.asList(nums[l], nums[r], nums[i]));
                    res.add(cur);

                    while (l < nums.length - 1 && nums[l] == nums[l+1]) l++;
                    while (r > 0 && nums[r] == nums[r-1]) r--;

                    l++;
                    r--;
                }
            }
        }
        return res;
    }
}
