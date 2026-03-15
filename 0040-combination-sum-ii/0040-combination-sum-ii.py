class Solution(object):
    def combinationSum2(self, candidates, target):
        L=[]
        candidates.sort()
        def srh(s,i,t):
            if t==0:
                L.append(s)
                return 
            if t<0:
                return
            for j in range(i,len(candidates)):
                if j>i and candidates[j]==candidates[j-1]:
                    continue
                if candidates[j] > t:
                    return 
                srh(s+[candidates[j]],j+1,t-candidates[j])
        srh([],0,target)
        return L


        
