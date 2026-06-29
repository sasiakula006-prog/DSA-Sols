class Solution(object):
    def majorityElement(self, nums):
        r = len(nums)//3
        d = defaultdict(int)
        v = set()
        ans = []
        for val in nums:
            d[val]+=1
            if d[val]>r and val not in v:
                v.add(val)
                ans.append(val)
        return ans