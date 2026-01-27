class Solution(object):
    def nextGreaterElement(self, n):
        l = [int(x) for x in str(n)]
        p = -1
        b = len(l)
        for i in range(b-2,-1,-1):
            if l[i] < l[i+1]:
                p = i
                break
        if p ==-1:
            return p
        for i in range(b-1,p,-1):
            if l[i] > l[p]:
                l[i],l[p] = l[p],l[i]
                break
        l[p+1:] = l[p+1:][::-1]
        ans =int(''.join(map(str,l)))
        if ans <= 2**31-1:
            return ans
        return -1
