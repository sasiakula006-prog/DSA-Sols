class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1:
            return 0
        f = False
        idx = 0
        if abs(nums[0]-nums[1]) == 1:
            p = nums[1]-nums[0]
        else:
            f = True
            idx = 1
            p = nums[2]-nums[1]

        for i in range(2,n):
            if nums[i]-nums[i-1] == p:
                continue
            else:
                if f :
                    return -1
                else:
                    if (p==-1 and nums[i]==n-1 and nums[i-1]== 0 ) or (p==1 and nums[i] == 0 and nums[i-1]==n-1):
                        f = True
                        idx = i
                    else:
                        return -1
        
        if  f :
            if p==-1:
                return min(idx+1,n-idx+1)
            else:
                return min(idx,n-idx+2)
        else:
            if nums[0]==0:
                return 0
            else:
                return 1
        
            
