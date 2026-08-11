class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)

        for s in strs:
            sorted_s = "".join(sorted(s))
            seen[sorted_s].append(s)
        return list(seen.values())