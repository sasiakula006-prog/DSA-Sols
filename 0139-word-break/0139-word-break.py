class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [-1]*n
        def f(i):
            if i >=n:
                return True
            if dp[i] !=-1:
                return dp[i]
            for w in wordDict:
                if s[i:i+len(w)]==w and f(i+len(w)):
                    dp[i] = True
                    return True
            dp[i] = False
            return False
        return f(0)