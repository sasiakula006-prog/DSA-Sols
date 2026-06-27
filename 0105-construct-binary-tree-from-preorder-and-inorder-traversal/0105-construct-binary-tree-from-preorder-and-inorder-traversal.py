# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        d = defaultdict(int)
        n = len(inorder)
        for i in range(n):
            d[inorder[i]] = i
        def dfs(ps,pe,ins,ine):
            if ps>pe or ins>ine:
                return None
            cur = TreeNode(preorder[ps]) 
            l = d[cur.val]-ins
            cur.left = dfs(ps+1,ps+l,ins,d[cur.val]-1)
            cur.right = dfs(ps+l+1,pe,d[cur.val]+1,ine)
            return cur
        return dfs(0,n-1,0,n-1)