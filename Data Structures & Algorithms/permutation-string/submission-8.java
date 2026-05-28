class Solution {
    public boolean checkInclusion(String s1, String s2) {
        if (s1.length() > s2.length()) return false;

        int[] countS1 = new int[26];
        int[] countWindow = new int[26];

        // record the character counts of s1 and first len(s1) characters in s2
        for (int i=0;i<s1.length();i++){
            countS1[s1.charAt(i) - 'a']++;
            countWindow[s2.charAt(i) - 'a']++;
        }

        for (int i=s1.length();i<s2.length();i++){
            // compare if current counts match -> if yes then return true
            if (Arrays.equals(countS1, countWindow)) return true;

            // otherwise, add the current character to window, remove left character from window
            countWindow[s2.charAt(i) - 'a']++;
            countWindow[s2.charAt(i - s1.length()) - 'a']--;
        }

        // in the end, there's a final comparison as the loop only added the final characters
        // but never compared the last window version
        return Arrays.equals(countS1, countWindow);
    }
}

