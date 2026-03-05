from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        return (
            p.val == q.val
            and self.isSameTree(p.left, q.left)
            and self.isSameTree(p.right, q.right)
        )

def build_tree(level_order):
    """Builds a binary tree from a level-order list like [1,2,3,None,4]."""
    if not level_order:
        return None
    if level_order[0] is None:
        return None

    root = TreeNode(level_order[0])
    q = deque([root])
    i = 1

    while q and i < len(level_order):
        node = q.popleft()

        # left
        if i < len(level_order) and level_order[i] is not None:
            node.left = TreeNode(level_order[i])
            q.append(node.left)
        i += 1

        # right
        if i < len(level_order) and level_order[i] is not None:
            node.right = TreeNode(level_order[i])
            q.append(node.right)
        i += 1

    return root

if __name__ == "__main__":
    sol = Solution()

    # Example 1
    p = build_tree([1, 2, 3])
    q = build_tree([1, 2, 3])
    print(sol.isSameTree(p, q))  # expected: True

    # Example 2
    p = build_tree([1, 2])
    q = build_tree([1, None, 2])
    print(sol.isSameTree(p, q))  # expected: False

    # Example 3
    p = build_tree([1, 2, 1])
    q = build_tree([1, 1, 2])
    print(sol.isSameTree(p, q))  # expected: False

    # Extra: both empty
    p = build_tree([])
    q = build_tree([])
    print(sol.isSameTree(p, q))  # expected: True