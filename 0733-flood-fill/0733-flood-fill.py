class Solution(object):
    def floodFill(self, image, sr, sc, color):
        q = deque()
        m = len(image)
        n = len(image[0])
        if image[sr][sc]==color:
            return image
        col = image[sr][sc]
        image[sr][sc]=color
        q.append((sr,sc))
        d = [(0,1),(0,-1),(1,0),(-1,0)]
        while q:
            r,c=q.popleft()
            for dr,dc in d:
                nr = r+dr
                nc = c+dc
                if 0<=nr<m and 0<=nc<n and image[nr][nc]== col:
                    q.append((nr,nc))
                    image[nr][nc] =color
        return image