class Solution(object):
    def isBipartite(self, graph):
        #bfs
        n = len(graph)
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
        return True