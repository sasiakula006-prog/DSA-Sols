class Solution(object):
    def sumAndMultiply(self, s, queries):
        n = len(s)
        d = {}
        s0 = ''
        j = 0
        en = [-1]*n
        st = [-1]*n
        pre = [0]
        for i in range(n):
            if s[i] != '0':
                s0+=s[i]
                d[i] = j
                j+=1
                pre.append(pre[-1]+ord(s[i])-48)
                en[i] = i
            else:
                pre.append(pre[-1])
                en[i] = en[i-1]
        
        st[n-1] = (-1 if s[n-1]=='0' else n-1)
        for i in range(n-2,-1,-1):
            if s[i] != '0':
                st[i] = i
            else:
                st[i] = st[i+1]
        
        ans = []
        MOD = 10**9 + 7

        pow10 = [1] * (len(s0) + 1)
        for i in range(1, len(s0) + 1):
            pow10[i] = (pow10[i-1] * 10) % MOD

        pref_num = [0] * (len(s0) + 1)
        for i in range(len(s0)):
            pref_num[i+1] = (pref_num[i] * 10 + int(s0[i])) % MOD

        for a,b in queries:
            if st[a] !=-1 and st[a] <= b:
                l = d[st[a]]
                r = d[en[b]]
                num = (pref_num[r+1] - pref_num[l] * pow10[r - l + 1]) % MOD
            else:
                num = 0
            t = pre[b+1] - pre[a]
            ans.append((t*num)%MOD) 
        return ans

        