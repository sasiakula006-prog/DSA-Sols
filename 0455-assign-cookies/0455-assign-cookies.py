class Solution(object):
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()
        m = len(g)
        n = len(s)
        i = j = 0
        while i<m and j<n:
            if s[j]>=g[i]:
                i+=1
            j+=1
        return i