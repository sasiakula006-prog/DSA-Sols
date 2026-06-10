class Solution(object):
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()
        m = len(g)
        n = len(s)
        i = j= cnt =0
        while i<m and j<n:
            if s[j]>=g[i]:
                cnt+=1
                i+=1
                j+=1
            else:
                j+=1
        return cnt