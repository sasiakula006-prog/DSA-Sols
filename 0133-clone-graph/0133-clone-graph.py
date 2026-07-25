"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        q,clone = deque([node]),{node.val: Node(node.val,[])}
        while q:
            n = q.popleft()
            n_clone = clone[n.val]
            for v in n.neighbors:
                if v.val not in clone:
                    clone[v.val] = Node(v.val,[])
                    q.append(v)
                n_clone.neighbors.append(clone[v.val])
        return clone[node.val]   