class Solution(object):
    def maxSubarraySum(self, nums, k):
        n = len(nums)
        def f(task):
            didnt=ans=done=doing = -1e20
            for x in nums:
                if task=='m':
                    y = x*k
                else:
                    if x>=0:
                        y = x//k
                    else:
                        y = -((-x)//k)
                n_didnt = max(x,didnt+x)
                n_doing = max(y,didnt+y,doing+y)
                n_done = max(x,done+x,doing+x)
                didnt,doing,done = n_didnt,n_doing,n_done
                ans = max(ans,didnt,doing,done)
            return ans

        return max(f('m'),f('d'))