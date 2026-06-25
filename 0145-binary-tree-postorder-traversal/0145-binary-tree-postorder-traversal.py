# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        ans= []
        def dfs(cur):
            if not cur:
                return 
            dfs(cur.left)
            dfs(cur.right)
            ans.append(cur.val)
        dfs(root)
        return ans
        