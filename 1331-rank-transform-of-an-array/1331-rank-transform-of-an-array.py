class Solution(object):
    def arrayRankTransform(self, arr):
        n = len(arr)
        nums = sorted(arr)
        d = {}
        r = 1
        ans = [ -1]*n
        for val in nums:
            if val in d:
                continue
            else:
                d[val]=r
                r+=1
        for i in range(n):
            ans[i] = d[arr[i]]
        return ans