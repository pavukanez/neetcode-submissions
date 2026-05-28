class Solution {
    public boolean checkInclusion(String s1, String s2) {
        

        for (int i=0;i<s2.length() - s1.length() + 1;i++){
            int[] count = new int[26];
            for (char c:s1.toCharArray()){
                count[c - 'a']++;
            }

            String s = s2.substring(i, i + s1.length());
            boolean flag = true;
            for (char c:s.toCharArray()){
                if (--count[c - 'a'] < 0) {
                    flag = false;
                    break;
                }
            }
            if (flag) return true;
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
