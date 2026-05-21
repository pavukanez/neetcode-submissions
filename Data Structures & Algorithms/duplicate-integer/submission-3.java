class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<int> seen = new HashSet<>();
        for (int num:nums){
            if (seen.get(num)) return true;
            seen.add(num);
        }
        return false;
    }
}