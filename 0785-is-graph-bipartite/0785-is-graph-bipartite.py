class Solution(object):
    def isBipartite(self, graph):
        #bfs
        '''n = len(graph)
        vis = [False]*n
        c = [0]*n
        for i in range(n):
            if not vis[i]:
                q = deque()
                q.append(i)
                vis[i] = True
                c[i]=0 
                while q:
                    a = q.popleft()
                    for v in graph[a]:
                        if not vis[v]:
                            vis[v] = True
                            c[v] = (1+c[a])%2
                            q.append(v)
                        else:
                            if c[v] == c[a]:
                                return False
        return True'''
        n = len(graph)
        vis = [False]*n
        color = [0]*n
        def dfs(i,c):
            vis[i] = True
            color[i] = c
            for nbr in graph[i]:
                if not vis[nbr]:
                    if dfs(nbr,1-c):
                        return True
                else:
                    if color[nbr] == color[i]:
                        return True
            return False
        for i in range(n):
            if not vis[i]:
                if dfs(i,0):
                    return False
        return True