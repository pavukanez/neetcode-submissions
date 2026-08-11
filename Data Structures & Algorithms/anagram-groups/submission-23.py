class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = dict()

        for s in strs:
            sorted_s = s.sort()
            res.setdefault(sorted_s, [])
            res[sorted_s].add(s)
        
        return res.values()
