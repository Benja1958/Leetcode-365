
from typing import Optional
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        #to slove this problem we use a stack to push the top elements and mantain the order of the traversal
        self.stack = []
        self.push_left(root)

    def push_left(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        node = self.stack.pop()
        if node.right:
            self.push_left(node.right)
        return node.val
           
    def hasNext(self) -> bool:
        return len(self.stack) > 0


def build_tree(level_order):
    if not level_order:
        return None
    if level_order[0] is None:
        return None

    root = TreeNode(level_order[0])
    q = deque([root])
    i = 1

    while q and i < len(level_order):
        node = q.popleft()

        if i < len(level_order) and level_order[i] is not None:
            node.left = TreeNode(level_order[i])
            q.append(node.left)
        i += 1

        if i < len(level_order) and level_order[i] is not None:
            node.right = TreeNode(level_order[i])
            q.append(node.right)
        i += 1

    return root


def run_leetcode_style(operations, args):
    result = []
    iterator = None

    for op, arg in zip(operations, args):
        if op == "BSTIterator":
            root = build_tree(arg[0])
            iterator = BSTIterator(root)
            result.append(None)
        elif op == "next":
            result.append(iterator.next())
        elif op == "hasNext":
            result.append(iterator.hasNext())
        else:
            raise ValueError(f"Unsupported operation: {op}")

    return result


if __name__ == "__main__":
    operations = [
        "BSTIterator",
        "next",
        "next",
        "hasNext",
        "next",
        "hasNext",
        "next",
        "hasNext",
        "next",
        "hasNext",
    ]
    args = [
        [[7, 3, 15, None, None, 9, 20]],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
    ]
    expected = [None, 3, 7, True, 9, True, 15, True, 20, False]

    actual = run_leetcode_style(operations, args)
    print(f"test 1: {actual} | expected: {expected}")
    assert actual == expected, "test 1 failed"

    operations2 = ["BSTIterator", "hasNext", "next", "hasNext"]
    args2 = [[[1]], [], [], []]
    expected2 = [None, True, 1, False]

    actual2 = run_leetcode_style(operations2, args2)
    print(f"test 2: {actual2} | expected: {expected2}")
    assert actual2 == expected2, "test 2 failed"

    print("All BSTIterator tests passed.")
