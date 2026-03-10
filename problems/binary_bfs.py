from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #since we want level order traversal, we willuse bfs
        #in every level, pick the rightmost node and add it to the list result
        
        if not root:
            return []

        result = []
        
        queue = deque([root])

        while queue:
            #get the length of the queue
            level_len = len(queue)
            for i in range(level_len):
                node = queue.popleft()

                #if we get to the last node, we append it to the result list(furthest to right)
                if i == level_len - 1:
                    result.append(node.val)

                #append the children, left first then right
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return result
    
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        #use bfs
        if not root:
            return []
        
        q = deque([root])
        result = []

        while q:
            level_len = len(q)
            total = 0

            for _ in range(level_len):
                node = q.popleft()
                total += node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            avg = total / level_len
            result.append(avg)

        return result


def build_tree(level_order: List[Optional[int]]) -> Optional[TreeNode]:
    """Build a binary tree from level-order values (use None for missing nodes)."""
    if not level_order:
        return None
    if level_order[0] is None:
        return None

    root = TreeNode(level_order[0])
    queue = deque([root])
    i = 1

    while queue and i < len(level_order):
        node = queue.popleft()

        if i < len(level_order) and level_order[i] is not None:
            node.left = TreeNode(level_order[i])
            queue.append(node.left)
        i += 1

        if i < len(level_order) and level_order[i] is not None:
            node.right = TreeNode(level_order[i])
            queue.append(node.right)
        i += 1

    return root


if __name__ == "__main__":
    sol = Solution()

    right_side_view_tests = [
        {"tree": [1, 2, 3, None, 5, None, 4], "expected": [1, 3, 4]},
        {"tree": [1, None, 3], "expected": [1, 3]},
        {"tree": [], "expected": []},
        {"tree": [1, 2, None, 3, None, 4], "expected": [1, 2, 3, 4]},
        {"tree": [1, 2, 3, 4], "expected": [1, 3, 4]},
    ]

    for i, tc in enumerate(right_side_view_tests, start=1):
        root = build_tree(tc["tree"])
        actual = sol.rightSideView(root)
        print(f"rightSideView test {i}: {actual} | expected: {tc['expected']}")
        assert actual == tc["expected"], f"rightSideView test {i} failed"

    print("All rightSideView tests passed.")

    average_of_levels_tests = [
        {"tree": [3, 9, 20, None, None, 15, 7], "expected": [3.0, 14.5, 11.0]},
        {"tree": [3, 9, 20, 15, 7], "expected": [3.0, 14.5, 11.0]},
        {"tree": [1], "expected": [1.0]},
        {"tree": [], "expected": []},
        {"tree": [5, 14, -3], "expected": [5.0, 5.5]},
    ]

    for i, tc in enumerate(average_of_levels_tests, start=1):
        root = build_tree(tc["tree"])
        actual = sol.averageOfLevels(root)
        print(f"averageOfLevels test {i}: {actual} | expected: {tc['expected']}")
        assert actual == tc["expected"], f"averageOfLevels test {i} failed"

    print("All averageOfLevels tests passed.")
