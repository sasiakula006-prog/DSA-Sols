# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        ans = []
        def dfs(cur):
            if cur:
                ans.append(cur.val)
                if cur.left:
                    dfs(cur.left)
                if cur.right:
                    dfs(cur.right)
        dfs(root)
        return ans