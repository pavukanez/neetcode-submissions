class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = dict()

        for s in strs:
            sorted_s = "".join(sorted(s))
            res.setdefault(sorted_s, [])
            res[sorted_s].append(s)
        
        return res.values()
