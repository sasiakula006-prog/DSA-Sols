class Solution(object):
    def topKFrequent(self, nums, k):
        d = Counter(nums)
        h = []
        ans=[]
        for v,c in d.items():
            heapq.heappush(h,(-c,v))
        while k:
            c,v = h[0]
            ans.append(v)
            heapq.heappop(h)
            k-=1
        return ans
        