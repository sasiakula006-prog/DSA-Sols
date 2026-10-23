class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        lis = []
        for i,val in enumerate(nums):
            if val==i:
                continue
            else:
                lis.append(val)
        if not lis:
            return 0
        ans = lis[-1]
        for val in lis:
            ans &= val
        return ans