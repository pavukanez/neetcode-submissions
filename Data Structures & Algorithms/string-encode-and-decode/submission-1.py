class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + s
        return res

    # s = 5hello5world
    def decode(self, s: str) -> List[str]:
        pos = 0
        res = []
        while pos < len(s):
            str_len = int(s[pos])
            res.append(s[pos + 1:pos + 1 + str_len])
            pos += str_len + 1
        return res
    
