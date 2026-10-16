class DSU:

    def __init__(self, n):
        self.parents = list(range(n))
        self.ranks = [0] * n
    
    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)

        if px == py:
            return False
        
        if self.ranks[px] < self.ranks[py]:
            self.parents[px] = py
            self.ranks[py] += self.ranks[px]
        else:
            self.parents[py] = px
            self.ranks[px] += self.ranks[py]
        return True

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        dsu = DSU(n)

        emailToAcc = defaultdict(int)

        for i, acc in enumerate(accounts):
            for email in acc[1:]:
                if email in emailToAcc:
                    dsu.union(i, emailToAcc[email])
                else:
                    emailToAcc[email] = i

        emailGroups = defaultdict(list)

        for email, accIdx in emailToAcc.items():
            leader = dsu.find(emailToAcc[email])
            emailGroups[leader].append(email)

        res = []

        for accIdx, emails in emailGroups.items():
            res.append([accounts[accIdx][0]] + sorted(emails))

        return res 