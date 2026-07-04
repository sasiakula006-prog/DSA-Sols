class Solution(object):
    def numOfStrings(self, patterns, word):
        cnt = 0
        for s in patterns:
            if s in word:
                cnt+=1
        return cnt
        