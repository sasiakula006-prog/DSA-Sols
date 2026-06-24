class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums2)<len(nums1):
            return self.findMedianSortedArrays(nums2,nums1)
        n1 = len(nums1)
        n2 = len(nums2)
        mini = -1e9
        maxi = 1e9
        l = 0
        h = n1
        while l<=h:
            c1 = (l+h)//2
            c2 = ((n1+n2+1)//2)-c1 

            l1 = nums1[c1-1] if c1 else mini
            r1 = nums1[c1] if c1 !=n1 else maxi
            l2 = nums2[c2-1] if c2 else mini
            r2 = nums2[c2] if c2 != n2 else maxi

            if l1<=r2 and l2<=r1:
                if (n1+n2)%2:
                    return max(l1,l2)
                return (max(l1,l2)+min(r1,r2))/2.0
            elif l2>r1:
                l = c1+1
            else:
                h = c1-1
        return 0


        