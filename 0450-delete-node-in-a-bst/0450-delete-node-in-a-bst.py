# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode | None, key: int) -> TreeNode | None:

        def r_most(node):
            pre = None
            while node.right:
                pre = node
                node = node.right
            return (pre,node)
        
        n = root
        p = None
        d = 0
        while n:
            if n.val == key:
                if n.left:
                    pre,req = r_most(n.left)
                    if d==1:
                        p.right = n.left
                    elif d==-1:
                        p.left = n.left
                    else:
                        root = n.left
                    if n.right:
                        req.right = n.right
                elif n.right:
                    if d==1:
                        p.right = n.right
                    elif d==-1:
                        p.left = n.right
                    else:
                        root = n.right
                else:
                    if d==1:
                        p.right = None
                    elif d==-1:
                        p.left = None
                    else:
                        return None
                    
                break
            elif n.val<key:
                p = n
                d = 1
                n = n.right        
            else:
                p = n
                d = -1
                n = n.left
                
        return root
