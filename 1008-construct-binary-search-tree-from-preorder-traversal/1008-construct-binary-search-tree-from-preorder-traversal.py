# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: list[int]) -> TreeNode | None:
        inorder = sorted(preorder)
        inmap = defaultdict(int)
        for i in range(len(inorder)):
            inmap[inorder[i]] = i
        
        def build(inst,ined,pst,ped):
            inleft = inmap[preorder[pst]] - inst
            n = TreeNode(preorder[pst])
            if inleft:
                n.left = build(inst,inmap[preorder[pst]]-1,pst+1,pst+inleft)
            if ined>inmap[preorder[pst]]:
                n.right = build(inmap[preorder[pst]]+1,ined,pst+inleft+1,ped)
            return n
        
        return build(0,len(inorder)-1,0,len(inorder)-1)