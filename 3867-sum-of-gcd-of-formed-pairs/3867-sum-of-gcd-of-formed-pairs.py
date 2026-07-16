from math import gcd
class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        n = len(nums)
        mx = nums[0]
        prefixGcd = [-1]*n
        prefixGcd[0] = nums[0]
        for i in range(1,n):
            mx = max(mx,nums[i])
            prefixGcd[i] = gcd(nums[i],mx)
        prefixGcd.sort()
        l=0
        r=n-1
        ans = 0
        while l<r:
            ans += gcd(prefixGcd[l],prefixGcd[r])
            l+=1
            r-=1
        return ans