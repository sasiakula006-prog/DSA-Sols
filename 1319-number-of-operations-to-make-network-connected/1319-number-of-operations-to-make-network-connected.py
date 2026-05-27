class Solution(object):
    def makeConnected(self, n, connections):
        cn = len(connections)
        vis = [False]*n
        if cn<n-1:
            return -1
        adj = [[]*n for _ in range(n)]
        for u,v in connections:
            adj[u].append(v)
            adj[v].append(u)
        def dfs(i):
            vis[i] = True
            for val in adj[i]:
                if not vis[val]:
                    dfs(val)
        c = 0
        q = deque()
        for i in range(n):
            if not vis[i]:
                q.append(i)
                vis[i] = True
                while q:
                    u = q.popleft()
                    for v in adj[u]:
                        if not vis[v]:
                            vis[v] = True
                            q.append(v)
                c+=1
        return c-1
