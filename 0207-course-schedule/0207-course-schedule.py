class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        #DFS
        d = defaultdict(list)
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
        return True
        