class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        deleted = False

        while l < r:
            if s[l] != s[r]:
                if deleted:
                    return False
                deleted = True
            l += 1
            r -= 1
        
        return True