# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        maxi = defaultdict(int)
        mini = defaultdict(int)
        def dfs(node):
            if not node:
                return True
            if not (dfs(node.left) and dfs(node.right)):
                return False
            if (node.right and mini[node.right] <= node.val) or (node.left and maxi[node.left]>= node.val):
                return False
            if node.right:
                maxi[node] = maxi[node.right]
            else:
                maxi[node] = node.val
            if node.left:
                mini[node] = mini[node.left]
            else:
                mini[node] = node.val
            return True
        return dfs(root)
