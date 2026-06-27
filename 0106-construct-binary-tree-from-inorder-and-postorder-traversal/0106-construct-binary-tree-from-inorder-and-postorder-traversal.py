# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        postorder.reverse()
        n = len(inorder)
        d = defaultdict(int)
        for i in range(n):
            d[inorder[i]] = i
        def dfs(ps,pe,ins,ine):
            if ps>pe or ins>ine:
                return None
            cur = TreeNode(postorder[ps])
            rl = ine-d[cur.val]
            cur.right = dfs(ps+1,ps+rl,d[cur.val]+1,ine)
            cur.left = dfs(ps+rl+1,pe,ins,d[cur.val]-1)
            return cur
        return dfs(0,n-1,0,n-1)