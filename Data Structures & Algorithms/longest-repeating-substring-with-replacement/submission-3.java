class Solution {
    public int characterReplacement(String s, int k) {
        Map<Character, Integer> map = new HashMap<>();
        int mostFreq = 0, l = 0, r = 0;

        while (r < s.length()){
            map.put(s.charAt(r), map.getOrDefault(s.charAt(r), 0) + 1);
            mostFreq = Math.max(mostFreq, map.get(s.charAt(r)));

            // If window is invalid, shrink from left
            if ((r - l + 1) - mostFreq > k){
                map.put(s.charAt(l), map.get(s.charAt(l)) - 1);
                l++;
            }
            r++;
        }
        return r - l;
    }
}