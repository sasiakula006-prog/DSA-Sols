class Solution(object):
    def minAddToMakeValid(self, s):
        c=[]
        for val in s:
            if val=='(':
                c.append(val)
            else:
                if c and c[-1]=='(':
                    c.pop()
                else:
                    c.append(val)
        return len(c)