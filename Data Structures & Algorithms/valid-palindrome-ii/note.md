# Problem statement

You are given a string s, return true if the s can be a palindrome after deleting at most one character from it.

A palindrome is a string that reads the same forward and backward.

Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).

Example 1:

Input: s = "aca"

Output: true
Explanation: "aca" is already a palindrome.

Example 2:

Input: s = "abbadc"

Output: false
Explanation: "abbadc" is not a palindrome and can't be made a palindrome after deleting at most one character.

Example 3:

Input: s = "abbda"

Output: true
Explanation: "We can delete the character 'd'.

Constraints:

1 <= s.length <= 100,000

s is made up of only lowercase English letters.

# Brute force
iterate s
- build a new string without current character as if skipping it by choice
- check if new string and its reversed version is same -> return True 

Why True? 
- if s is already palindrome: we either deleted middle character if odd length ("aba") or even length ("abba")
- if s not palindrome: we would inevitably build a new substring wihout the problematic character
    
return False once processed all possibilites

TC: O(n^2)
SC: O(n)

# Two pointers
- use two pointers at l = 0, r = len(s) - 1
- compare the characters at those indexes
    - if not same -> 2 choices
        - skip left character: check if string from l + 1 to r is palindrome
        - or skip right character: check if string from l to r - 1 is palindrome
    - if same: move l and r to mid
- return True as processed all characters

TC: O(n)

SC: O(1)

```
def validPalindrome(self, s: str) -> bool:
    def is_palindrome(l , r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    l, r = 0, len(s) - 1

    while l < r:
        if s[l] != s[r]:
            return is_palindrome(l + 1, r) or is_palindrome(l, r - 1)
        l += 1
        r -= 1
    return True
```