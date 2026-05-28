class Solution(object):
    def accountsMerge(self, accounts):
        n = len(accounts)
        parent = [i for i in range(n)]
        def find(i):
            if i == parent[i]:
                return i
            parent[i] = find(parent[i])
            return parent[i]
        def union(c,p):
            parent[find(c)] = find(p)
        owner = defaultdict(list)
        for i,account in enumerate(accounts):
            for email in account[1:]:
                if email in owner:
                    union(i,owner[email])
                owner[email] = i
        data = defaultdict(list)
        for email,holder in owner.items():
            data[find(holder)].append(email)
        ans = []
        for name,emails in data.items():
            ans.append([accounts[name][0]]+sorted(emails))
        return ans
        