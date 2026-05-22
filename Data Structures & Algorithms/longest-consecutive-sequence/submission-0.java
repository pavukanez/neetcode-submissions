class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> seen = new HashSet<>();
        for (int num:nums){
            seen.add(num);
        }
        int res = 0;
        for (int num:nums){
            if (seen.contains(num-1)) continue;

            int curLen = 0;
            int temp = num;
            while (seen.contains(temp)){
                curLen++;
                res = Math.max(res, curLen);
                temp++;
            }
        }

        return res;
    }
    
}
