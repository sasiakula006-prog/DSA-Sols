class Solution(object):
    def combinationSum(self, candidates, target):
        L=[]
        l = len(candidates)
        def srh(i,s,t):
            if t==0:
                L.append(s[:])
                return 
            if t<0 or i>=l:
                return           
            s.append(candidates[i])
            srh(i,s,t-candidates[i])
            s.pop()
            srh(i+1,s,t)
            return L
        return srh(0,[],target)
            
        