class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        incoming = [0] * (n + 1)
        outgoing = [0] * (n + 1)

        for p1, p2 in trust:
            incoming[p2] += 1
            outgoing[p1] += 1
        
        for i in range(1, n+1):
            if incoming[i] == n - 1 and outgoing[i] == 0:
                return i
        return -1