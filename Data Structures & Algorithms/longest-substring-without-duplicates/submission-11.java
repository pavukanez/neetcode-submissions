class Solution {
    public int lengthOfLongestSubstring(String s) {
        int maxLen = 0, l = 0, r = 0;
        Set<Character> seen = new HashSet<>();

        while (r < s.length()){
            // R character not seen -> substring valid -> add R character to seen -> expand 
            if (!seen.contains(s.charAt(r))){
                seen.add(s.charAt(r++));
                maxLen = Math.max(maxLen, r - l);
            }
            // R character seen -> substring invalid -> remove L character from seen to shrink substring
            else {
                seen.remove(s.charAt(l++));
            }
        }
        return maxLen;

    }
}