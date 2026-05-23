class Solution {
    public boolean isPalindrome(String s) {
        int l = 0;
        int r = s.length() - 1;

        boolean atLeastOneAlphaNumChar = false;
        for (char c:s.toCharArray()){
            if (Character.isLetterOrDigit(c)) atLeastOneAlphaNumChar = true;
        }
        if (!atLeastOneAlphaNumChar) return false;

        while (l <= r){
            while (l < s.length() - 1 && !Character.isLetterOrDigit(s.charAt(l))){
                l++;
            }
            while (r > 0 && !Character.isLetterOrDigit(s.charAt(r))){
                r--;
            }
            if (Character.toLowerCase(s.charAt(l)) != Character.toLowerCase(s.charAt(r))){
                return false;
            }

            l++;
            r--;
        }
        return true;
    }
}
