class Solution(object):
    def removeCoveredIntervals(self, intervals):
        intervals.sort(key = lambda x:x[0])
        prev0,prev1 = intervals[0]
        cnt = 1
        for s,e in intervals[1:]:
            if prev0 < s:
                if e<=prev1:
                    continue
                else:
                    prev0,prev1 = s,e
                    cnt+=1
            else:
                if e>prev1:
                    prev1 = e
        return cnt
        