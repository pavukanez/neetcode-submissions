class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        visit = set()

        res = []
        for u, v in edges:
            if u in visit and v in visit:
                res = [u, v]
            visit.add(u)
            visit.add(v)
        
        return res