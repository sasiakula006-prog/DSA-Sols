class Solution(object):
    def removeDuplicateLetters(self, s):
        d = defaultdict(int)
        vis = set()
        for val in s:
            d[val] += 1
        
        stack = []
        for a in s:
            d[a]-=1
            if a in vis:
                continue
            while stack and ord(stack[-1])>ord(a) and d[stack[-1]]>0:
                b = stack.pop()
                vis.remove(b)
            stack.append(a)
            vis.add(a)
        return ''.join(stack)