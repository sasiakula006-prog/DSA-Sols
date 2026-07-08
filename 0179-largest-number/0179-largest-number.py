class Solution(object):
    def largestNumber(self, nums):
        l = [str(num) for num in nums]
        l.sort(key = lambda x :x*10 ,reverse = True)
        if l[0] == '0':
            return '0'
        return ''.join(l)
        