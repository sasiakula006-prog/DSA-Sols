class Solution(object):
    def findKthPositive(self, arr, k):
        l = 0
        h = len(arr)-1
        if arr[0]-1>=k:
            return k
        ans = 0
        while l<=h:
            mid = (l+h)//2
            if arr[mid]-(mid+1)>=k:
                h = mid-1
            else:
                ans = mid
                l = mid+1
        return  k+ans+1
        