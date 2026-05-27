class Solution(object):
    def makeConnected(self, n, connections):
        cn = len(connections)
        vis = [False]*n
        if cn<n-1:
            return -1
        adj = defaultdict(list)
        for u,v in connections:
            adj[u].append(v)
            adj[v].append(u)
        def dfs(i):
            vis[i] = True
            for val in adj[i]:
                if not vis[val]:
                    dfs(val)
        c = 0
        for i in range(n):
            if not vis[i]:
                dfs(i)
                c+=1
        return c-1
