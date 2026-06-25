# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        if not root:
            return []
        d = defaultdict(list)
        self.length = 0
        def dfs(cur,l):
            if not cur:
                return
            self.length = max(self.length,l)
            d[l].append(cur.val)
            dfs(cur.left,l+1)
            dfs(cur.right,l+1)
        dfs(root,0)
        ans = [[]for _ in range(self.length+1)]
        for level in d.keys():
            ans[level] += d[level]
        return ans
