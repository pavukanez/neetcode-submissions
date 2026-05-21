class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> seen = new HashMap<>();
        for (int i=0;i<nums.length;i++){
            int diff = target - nums[i];
            if (seen.containsKey(diff)){
                int[] res = new int[2];
                res[0] = i;
                res[1] = seen.get(diff);
                return res;
            }
            seen.put(nums[i], i);
        }

        return new int[2];
    }
}
