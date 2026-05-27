class Solution {
    public int characterReplacement(String s, int k) {
        int[] count = new int[26];
        int l = 0, mostFreq = 0, maxLen = 0;

        while (r < s.length()){
            map[s.charAt(r) - 'A']++;
            mostFreq = Math.max(mostFreq, map[s.charAt(r) - 'A']);

            if ((r - l + 1) - mostFreq > k){
                count[s.charAt(l++) - 'A']--;
            }
            maxLen = Math.max(maxLen, r - l + 1);
        }

        return maxLen;
    }
}
