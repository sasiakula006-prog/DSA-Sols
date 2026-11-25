
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        lis = []
        def dfs(n):
            if n.left:
                dfs(n.left)
            lis.append(n.val)
            if n.right:
                dfs(n.right)

        dfs(root)
        return lis[k-1]
