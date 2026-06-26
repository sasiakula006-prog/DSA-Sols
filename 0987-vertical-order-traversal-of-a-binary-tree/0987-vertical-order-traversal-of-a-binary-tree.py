# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def verticalTraversal(self, root):
        d = defaultdict(lambda:defaultdict(list))
        self.maxi,self.mini = 0,0
        def dfs(cur,b,v):
            if not cur:
                return 
            self.maxi = max(self.maxi,b)
            self.mini = min(self.mini,b)
            d[b][v].append(cur.val)
            dfs(cur.left,b-1,v+1)
            dfs(cur.right,b+1,v+1)
        dfs(root,0,0)
        ans = [[] for _ in range(self.maxi-self.mini+1)]
        for i in d.keys():
            for v in sorted(d[i].keys()):
                d[i][v].sort()
                ans[i-self.mini] += d[i][v]
        return ans
        