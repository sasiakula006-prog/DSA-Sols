class Solution(object):
    def minimumEffortPath(self, heights):
        m,n = len(heights),len(heights[0])
        h = [(0,0,0)]
        di = [(1,0),(0,1),(-1,0),(0,-1)]
        dis = [[float('inf')]*n for _ in range(m)]
        while h:
            l,r,c = heapq.heappop(h)
            if r==m-1 and c==n-1:
                return l
            if l >dis[r][c]:
                continue
            for dr,dc in di:
                nr,nc = r+dr,c+dc
                if 0<=nr<m and 0<=nc<n:
                    nl = max(l,abs(heights[nr][nc]-heights[r][c]))
                    if nl < dis[nr][nc]:
                        dis[nr][nc] = nl
                        heapq.heappush(h,(nl,nr,nc))
                
        
