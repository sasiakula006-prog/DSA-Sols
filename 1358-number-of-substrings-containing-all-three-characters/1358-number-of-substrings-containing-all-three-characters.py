class Solution(object):
    def numberOfSubstrings(self, s):
        n = len(s)
        cnt = 0
        i= 0
        d = {'a':-1,'b':-1,'c':-1}
        while i<n:
            d[s[i]] = i
            mf = min(d['a'],d['b'],d['c'])
            cnt += mf+1
            i+=1
        return cnt