class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    # s = 15#helloaaaaabbbbb5#world
    def decode(self, s: str) -> List[str]:
        pos = 0
        res = []

        while pos < len(s):
            # get the correct substring length (1 digit, 2 digit, etc)
            str_len = ""
            while s[pos] != "#":
                str_len += s[pos]
                pos += 1
            
            # subtract substring and add to res
            substr = s[1 + pos:1 + pos + int(str_len)]
            res.append(substr)
            
            # move pos to 
            pos += 1 + int(str_len)

        return res

