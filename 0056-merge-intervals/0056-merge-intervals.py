class Solution(object):
    def merge(self, intervals):
        intervals.sort(key = lambda x:x[0])
        ans = [intervals[0]]
        for i in range(1,len(intervals)):
            if intervals[i][0]<=ans[-1][-1]:
                if ans[-1][-1]<intervals[i][-1]:
                    ans[-1][-1] = intervals[i][-1]
            else:
                ans.append(intervals[i])
        return ans
        