class Solution(object):
    def letterCombinations(self, digits):
        n = len(digits)
        d = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        l = list(d.keys())
        L =[]
        def faah(s,i):
            if len(s)==n:
                L.append(s)
                s = ''
                return
            for val in d[digits[i]]:
                faah(s+val,i+1)
        faah('',0)
        return L