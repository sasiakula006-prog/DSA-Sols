# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        ans = []
        def go_down(n,v):
            if not n:
                return
            if v==0:
                ans.append(n.val)
                return
            if n.left:
                go_down(n.left,v-1)
            if n.right:
                go_down(n.right,v-1)
        def dfs(n):
            if not n:
                return -1
            if n==target:
                go_down(n,k)
                return k-1
            l = dfs(n.left)
            r = dfs(n.right)
            if l==0 or r==0:
                ans.append(n.val)
                return -1
            if l == -1 and r==-1:
                return -1
            if l !=-1:
                go_down(n.right,l-1)
                return l-1
            if r !=-1:
                go_down(n.left,r-1)
                return r-1
        dfs(root)
        return ans