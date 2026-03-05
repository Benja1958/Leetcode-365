from typing import Optional, List
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
    
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #we will have a base case that inverts the nodes
        #recusrcively call the fuunction with left and right
        if not root:
            return None
        
        #swap case
        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        #will compare tree at each given level
        #will create a helper function to helpe in 
        #Recursive approach 
        # def isMirror(a, b):
        #     if not a and not b:
        #         return True
        #     if not a or not b:
        #         return False
        #     if a.val != b.val:
        #         return False

        #     return isMirror(a.left, b.right) and isMirror(a.right, b.left)
        
        # return isMirror(root.left, root.right)


        #ITERATIVE APPROACH
        #using BFS
        queue = deque([(root.left, root.right)])
        while queue:
            a, b = queue.popleft()

            if not a and not b:
                continue
            if not a or not b:
                return False
            if a.val != b.val:
                return False
            
            queue.append((a.right, b.left))
            queue.append((a.left, b.right))
        return True
    
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #the first node in the preorder, is the rood node
        #all the nodes to the left of the root node from preorder in inorder will be on the left
        #all the nodes to the right of root node prom preorder in inorder will be on the right

        #base case for no tree
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])

        return root
    





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

def tree_to_level_order(root):
    """Converts a binary tree to level-order list format."""
    if not root:
        return []

    result = []
    q = deque([root])

    while q:
        node = q.popleft()
        if node is None:
            result.append(None)
            continue

        result.append(node.val)
        q.append(node.left)
        q.append(node.right)

    # remove trailing None values for cleaner output
    while result and result[-1] is None:
        result.pop()

    return result

if __name__ == "__main__":
    sol = Solution()

    #----------SAME TREE-----------
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

    #-----------INVERT TREE----------
    t = build_tree([4,2,7,1,3,6,9])
    inverted = sol.invertTree(t)
    print(tree_to_level_order(inverted))  # expected: [4, 7, 2, 9, 6, 3, 1]

    #----------SYMMETRIC TREE---------
    S = build_tree([1,2,2,3,4,4,3])
    print(sol.isSymmetric(S))

    #----------BUILD TREE (PREORDER + INORDER)---------
    build_tree_tests = [
        {
            "preorder": [3, 9, 20, 15, 7],
            "inorder": [9, 3, 15, 20, 7],
            "expected": [3, 9, 20, None, None, 15, 7],
        },
        {
            "preorder": [-1],
            "inorder": [-1],
            "expected": [-1],
        },
        {
            "preorder": [],
            "inorder": [],
            "expected": [],
        },
        {
            "preorder": [1, 2, 3],
            "inorder": [1, 2, 3],
            "expected": [1, None, 2, None, 3],
        },
    ]

    for i, tc in enumerate(build_tree_tests, start=1):
        built = sol.buildTree(tc["preorder"], tc["inorder"])
        actual = tree_to_level_order(built)
        print(f"buildTree test {i}: {actual} | expected: {tc['expected']}")
        assert actual == tc["expected"], f"buildTree test {i} failed"
    
