class Solution:
    def largestOddNumber(self, num: str) -> str:
        v = 0
        n = len(num)
        for i in range(n-1,-1,-1):
            if int(num[i])%2:
                return num[:i+1]
        return ""
