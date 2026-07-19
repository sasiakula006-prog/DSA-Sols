class Solution:
    def smallestSubsequence(self, s: str) -> str:
        d = defaultdict(int)
        for val in s:
            d[val] +=1
        vis = set()
        stack = []
        for val in s:
            d[val] -=1
            if val in stack:
                continue
            while stack and ord(stack[-1])> ord(val) and d[stack[-1]]>0:
                stack.pop()
            stack.append(val)
        return "".join(stack)
