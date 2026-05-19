class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        #DFS
        adj = [[] for _ in range(numCourses)]
        for val in prerequisites:
            adj[val[-1]].append(val[0])
        vis = [False]*numCourses
        path = [False]*numCourses
        def dfs(i):
            vis[i] = path[i] = True
            for val in adj[i]:
                if not vis[val]:
                    if dfs(val):
                        return True
                elif path[val]:
                    return True
            path[i] = False
            return False
        for i in range(numCourses):
            if not vis[i]:
                if dfs(i):
                    return False
        return True
        #BFS
        ''' d = defaultdict(list)
        indeg = [0]*numCourses
        for c,pre in prerequisites:
            d[pre].append(c)
            indeg[c]+=1
        cont = 0
        q = deque()
        for i in range(numCourses):
            if indeg[i]==0:
                q.append(i)
        while q:
            c = q.popleft()
            cont+=1
            for val in d[c]:
                indeg[val] -=1
                if indeg[val]==0:
                    q.append(val)
        return cont == numCourses'''