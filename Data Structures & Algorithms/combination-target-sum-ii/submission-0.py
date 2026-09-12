class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(i, subset, remain):
            if remain == 0:
                res.append(subset.copy())
                return
            
            for j in range(i, len(candidates)):
                if j > i and candidates[j - 1] == candidates[j]:
                    continue
                
                if remain - candidates[j] < 0:
                    break

                subset.append(candidates[j])
                dfs(j + 1, subset, remain - candidates[j])
                subset.pop()
            
        dfs(0, [], target)

        return res
