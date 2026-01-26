
class Solution(object):
    def findKthLargest(self, nums, k):
        heap = []
        for val in nums:
            heapq.heappush(heap,val)
            if len(heap) >k:
                heapq.heappop(heap)
        return heapq.heappop(heap)
        