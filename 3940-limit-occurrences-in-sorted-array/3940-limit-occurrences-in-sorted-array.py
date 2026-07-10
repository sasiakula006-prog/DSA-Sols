class Solution(object):
    def limitOccurrences(self, nums, k):
        freq = defaultdict(int)
        ans = []
        for val in nums:
            if freq[val]<k:
                freq[val]+=1
                ans.append(val)
        return ans
        