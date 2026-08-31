class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): 
            return False

        count1, count2 = [0] * 26, [0] * 26
        l = 0

        for i in range(len(s1)):
            count1[ord(s1[i]) - ord('a')] += 1

        for i in range(len(s1) - 1):
            count2[ord(s2[i]) - ord('a')] += 1

        for r in range(len(s1) - 1, len(s2)):
            count2[ord(s2[r]) - ord('a')] += 1

            is_same = True
            for i in range(26):
                if count1[i] != count2[i]:
                    is_same = False
                    break
            if is_same: 
                return True
            
            count2[ord(s2[l]) - ord('a')] -= 1
            l += 1
            
        return False
        
