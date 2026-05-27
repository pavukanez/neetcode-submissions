class Solution {
    public int lengthOfLongestSubstring(String s) {
        int maxLen = 0, l = 0, r = 0;
        Set<Character> seen = new HashSet<>();

        while (r < s.length()){
            if (!seen.contains(s.charAt(r))){
                seen.add(s.charAt(r++));
                maxLen = Math.max(maxLen, r - l + 1);
            }
            else {
                seen.remove(s.charAt(l++));
            }
        }
        return maxLen;

    }
}