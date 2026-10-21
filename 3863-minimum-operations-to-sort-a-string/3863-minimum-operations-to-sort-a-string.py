class Solution:
    def minOperations(self, s: str) -> int:
        if len(s)==2:
            if ord(s[0])>ord(s[-1]):
                return -1
            else:
                return 0
        maxi = 0
        mn,mx = 0,0
        mini = 30
        p=-1
        f = True
        for i,val in enumerate(s):
            c = ord(val) - ord('a')
            if c<p:
                f = False
            p = c
            if c<mini:
                mini = c
                mn = i
            if c>=maxi:
                maxi = c
                mx = i
        if f:
            return 0
        if mn ==0 or mx==len(s)-1:
            return 1
        if mn==len(s)-1 and mx ==0:
            return 3

        return 2
        