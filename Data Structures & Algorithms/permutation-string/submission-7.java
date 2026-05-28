class Solution {
    public boolean checkInclusion(String s1, String s2) {
        if (s1.length() > s2.length()) return false;

        int[] countS1 = new int[26];
        int[] countWindow = new int[26];

        for (int i=0;i<s1.length();i++){
            countS1[s1.charAt(i) - 'a']++;
            countWindow[s2.charAt(i) - 'a']++;
        }

        for (int i=s1.length();i<s2.length();i++){
            if (Arrays.equals(countS1, countWindow)) return true;

            countWindow[s2.charAt(i) - 'a']++;
            countWindow[s2.charAt(i - s1.length()) - 'a']--;
        }
        return Arrays.equals(countS1, countWindow);
    }
}

