class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [-1]*(target+1)
        def f(s):
            if s==0:
                return 1
            if dp[s] != -1:
                return dp[s]
            c = 0
            for i in range(n):
                if s>=nums[i]:
                    c += f(s-nums[i])
            dp[s] = c
            return c
        return f(target)