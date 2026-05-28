class Solution {
    public boolean checkInclusion(String s1, String s2) {
        int[] count = new int[26];
        for (char c:s1.toCharArray()){
            count[c - 'a']++;
        }

        for (int i=0;i<s2.length() - s1.length() + 1;i++){
            String s = s2.substring(i, i + s1.length());
            if (isAnagram(count, s)) return true;
        }
        return false;

    }

    public boolean isAnagram(int[] count, String s){
        for (char c:s.toCharArray()){
            if (--count[c - 'a'] < 0) return false;
        }
        return true;
    }

    
}
