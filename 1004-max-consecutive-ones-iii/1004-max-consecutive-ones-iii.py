class Solution(object):
    def longestOnes(self, nums, k):
        n = len(nums)
        r,l = 0,0
        maxi = 0

        while r<n:
            if nums[r]:
                maxi = max(maxi,r-l+1)
            else:
                if k:
                    k-=1
                    maxi = max(maxi,r-l+1)
                else:
                    while nums[l]:
                        l +=1
                    l+=1
            r+=1
        return maxi
