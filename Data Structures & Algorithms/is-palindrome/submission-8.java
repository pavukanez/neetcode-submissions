class Solution {
    public boolean isPalindrome(String s) {
        int l = 0, r = s.length() - 1;

        while (l <= r){
            // move left pointer to right until reach character that is either letter or digit, make sure it does not cross right pointer
            while (l < r && !Character.isLetterOrDigit(s.charAt(l))){
                l++;
            }
            // move right pointer to left until reach character that is either letter or digit, make sure it does not cross left pointer
            while (r > l && !Character.isLetterOrDigit(s.charAt(r))){
                r--;
            }
            // check if lowercase characters are equals
            if (Character.toLowerCase(s.charAt(l)) != Character.toLowerCase(s.charAt(r))){
                return false;
            }

            // move pointers towards middle
            l++;
            r--;
        }
        return true;
    }
}
