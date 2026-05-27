class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> seen = new HashSet<>();
        for (int num:nums){
            seen.add(num);
        }

        int res = 0;
        for (int num:nums){
            if (seen.contains(num-1)) continue;

            int cur = num, len = 0;
            while (seen.contains(cur)){
                len++;
                cur++;
            }
            res = Math.max(res, len);
        }
        return res;
    }
}
