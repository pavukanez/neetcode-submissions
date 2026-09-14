class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""

        for i in range(200):
            for j in range(1, len(strs)):
                if i == len(strs[j]) or strs[j][i] != strs[j - 1][i]:
                    return prefix
            prefix += strs[0][i]
        return prefix
