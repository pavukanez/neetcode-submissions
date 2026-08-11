class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        idx = 0
        res = []

        while idx < len(s):
            char_count = ""
            while s[idx] != '#':
                char_count += s[idx]
                idx += 1
            char_count = int(char_count)
            res.append(s[idx + 1: idx + 1 + char_count])
            
            idx += 1 + char_count
        return res
                
    
    
    
    
    