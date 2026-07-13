class Solution(object):
    def sequentialDigits(self, low, high):
        ans = []
        cnt = 0
        h = high
        while h>=1:
            h = h//10
            cnt+=1
    
        digits = '123456789'
        for l in range(2,cnt+1):
            for st in range(10-l):
                num = int(digits[st:st+l])
                if low<=num<=high:
                    ans.append(num)
        return ans

        
