class Solution {
    public int characterReplacement(String s, int k) {
        int[] count = new int[26];
        int l = 0, mostFreq = 0, maxLen = 0;

        for(int r=0;r<s.length();r++){
            count[s.charAt(r) - 'A']++;
            mostFreq = Math.max(mostFreq, count[s.charAt(r) - 'A']);

            // if window size - freq of most used char > k (need to replace more characters than allowed) -> shrink from left side
            if ((r - l + 1) - mostFreq > k){
                count[s.charAt(l) - 'A']--;
                l++;
            }
            maxLen = Math.max(maxLen, r - l + 1);
        }
        return maxLen;
    }
}