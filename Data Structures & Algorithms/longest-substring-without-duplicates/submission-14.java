class Solution {
    public int lengthOfLongestSubstring(String s) {
        Set<Character> seen = new HashSet<>();
        int l = 0, r = 0, maxLen = 0;

        while (r < s.length()){
            if (seen.contains(s.charAt(r))){
                seen.remove(s.charAt(l++));
            }
            else {
                seen.add(s.charAt(r));
            }

            maxLen = Math.max(maxLen, r - l + 1);
            r++;
        }
        return maxLen;
    }
}
