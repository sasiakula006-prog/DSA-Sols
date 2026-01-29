class Solution(object):
    def threeSum(self, nums):
        ans = []
        l = len(nums)
        nums.sort()
        for i in range(l):
            if i>0 and nums[i] == nums[i-1]:
                continue
            j = i+1
            k = l-1            
            while j<k:
                s = nums[i] + nums[j] + nums[k]
                if s > 0:
                    k -=1
                elif s<0:
                    j +=1
                else:
                    ans.append([nums[i],nums[j],nums[k]])
                    j +=1

                    while nums[j] == nums[j-1] and j<k:
                        j +=1

        return ans
         