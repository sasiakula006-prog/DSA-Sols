class Solution(object):
    def threeSum(self, nums,st,t):
        ans = []
        l = len(nums)
        for i in range(st+1,l):
            if i>st+1 and nums[i] == nums[i-1]:
                continue
            j = i+1
            k = l-1            
            while j<k:
                s = nums[i] + nums[j] + nums[k]
                if s > t:
                    k -=1
                elif s<t:
                    j +=1
                else:
                    ans.append([nums[st],nums[i],nums[j],nums[k]])
                    j +=1

                    while nums[j] == nums[j-1] and j<k:
                        j +=1

        return ans
    def fourSum(self, nums, target):
        nums.sort()
        ans = []
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            res = self.threeSum(nums,i,target-nums[i])
            if res:
                ans.extend(res)
        return ans
        