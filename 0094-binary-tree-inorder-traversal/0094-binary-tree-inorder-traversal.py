# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        ans = []
        def dfs(cur):
            if not cur:
                return
            dfs(cur.left)
            ans.append(cur.val)
            dfs(cur.right)
        dfs(root)
        return ans