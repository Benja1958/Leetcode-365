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
    
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #use bfs in the traversal
        #check if right to left, reverse the level
        if not root:
            return []

        result = []   
        left_to_right = True
        q = deque([root])

        #traverse the queue
        while q:
            level_len = len(q)

            #append the level nodes
            level = []
            for _ in range(level_len):
                node = q.popleft()
                level.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right) 
            
            if not left_to_right:
                level.reverse()
            result.append(level)
            left_to_right = not left_to_right

        return result
    
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #i will use bfs traversal where i will initialize a queue
        #in the traversal first i get the length of the queue before proceeding
        queue = deque([root])
        result = []

        while queue:
            len_q = len(queue)
            values = []

            #loop throufht that level
            for i in range(len_q):
                node = queue.popleft()
                if node:
                    values.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if values:
                result.append(values)

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

    zigzag_level_order_tests = [
        {"tree": [3, 9, 20, None, None, 15, 7], "expected": [[3], [20, 9], [15, 7]]},
        {"tree": [1], "expected": [[1]]},
        {"tree": [], "expected": []},
        {"tree": [1, 2, 3, 4, 5, 6, 7], "expected": [[1], [3, 2], [4, 5, 6, 7]]},
    ]

    for i, tc in enumerate(zigzag_level_order_tests, start=1):
        root = build_tree(tc["tree"])
        actual = sol.zigzagLevelOrder(root)
        print(f"zigzagLevelOrder test {i}: {actual} | expected: {tc['expected']}")
        assert actual == tc["expected"], f"zigzagLevelOrder test {i} failed"

    print("All zigzagLevelOrder tests passed.")

    level_order_tests = [
        {"tree": [3, 9, 20, None, None, 15, 7], "expected": [[3], [9, 20], [15, 7]]},
        {"tree": [1], "expected": [[1]]},
        {"tree": [], "expected": []},
        {"tree": [1, 2, 3, 4, None, None, 5], "expected": [[1], [2, 3], [4, 5]]},
    ]

    for i, tc in enumerate(level_order_tests, start=1):
        root = build_tree(tc["tree"])
        actual = sol.levelOrder(root)
        print(f"levelOrder test {i}: {actual} | expected: {tc['expected']}")
        assert actual == tc["expected"], f"levelOrder test {i} failed"

    print("All levelOrder tests passed.")
