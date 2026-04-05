class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        #DFS
        '''d = defaultdict(list)
        for val in prerequisites:
            d[val[0]].append(val[-1])
        
        t = set()
        def dfs(c):
            if not d[c]:
                return True
            if c in t:
                return False
            t.add(c)
            for val in d[c]:
                if not dfs(val):
                    return False 
            d[c]=[]          
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True'''
        #BFS
        d = defaultdict(list)
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
        return cont == numCourses