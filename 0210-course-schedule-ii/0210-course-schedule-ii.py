class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        ans=[]
        d = [0]*numCourses
        for a,_ in prerequisites:
            d[a]+=1
        ans =[a for a in range(numCourses) if d[a]==0]
        q = deque(ans)
        while q:
            node = q.popleft()
            for a,b in prerequisites:
                if b==node:
                    d[a]-=1
                    if d[a]==0:
                        ans.append(a)
                        q.append(a)
        if len(ans) != numCourses:
            return []
        return ans