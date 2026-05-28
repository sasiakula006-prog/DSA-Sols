class Solution(object):
    def removeStones(self, stones):
        max_row = 0
        max_col = 0
        n = len(stones)
        for i,j in stones:
            if i>max_row:
                max_row = i
            if j>max_col:
                max_col = j
        comp = max_row+max_col+2
        parent = [i for i in range(comp)]
        def find(i):
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])
            return parent[i]
        components = 0
        vis = set()
        for x,y in stones:
            (u,v) = (x,y+max_row+1)
            if u not in vis:
                vis.add(u)
                components +=1
            if v not in vis:
                vis.add(v)
                components +=1

        for x,y in stones:
            (u,v) = (x,y+max_row+1)
            pu = find(u)
            pv = find(v)
            if pu != pv:
                parent[pv]=pu
                components -=1
        return n-components

        