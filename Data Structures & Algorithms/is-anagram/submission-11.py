class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = dict()
        
        for i in range(len(s)):
            count.setdefault(s[i], 0)
            count[s[i]] += 1

            count.setdefault(t[i], 0)
            count[t[i]] -= 1
        
        for value in count.values():
            if value != 0:
                return False
        return True