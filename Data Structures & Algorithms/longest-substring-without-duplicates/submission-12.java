class Solution {
    public int lengthOfLongestSubstring(String s) {
        Set<Character> seen = new HashSet<>();
        int l = 0, maxLen = 0;

        for (int r = 0;r < s.length(); r++){
            if (seen.contains(s.charAt(r))){
                seen.remove(s.charAt(l++));
            }
            else {
                seen.add(s.charAt(r));
                maxLen = Math.max(maxLen, r - l + 1);
            }
        }
        return maxLen;
    }
}