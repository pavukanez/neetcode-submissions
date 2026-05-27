class Solution {
    public int lengthOfLongestSubstring(String s) {
        if (s.length() < 2) return s.length()

        int maxLen = 0, l = 0, r = 1;
        Set<Character> seen = new HashSet<>();

        while (r < s.length()){
            char c = s.charAt(r-1);

            if (seen.contains(c)){
                seen.remove(s.charAt(l));
                l++;
            }
            else {
                seen.add(c);
                r++;
                maxLen = Math.max(maxLen, seen.size());
            }
        }
        return maxLen;

    }
}
