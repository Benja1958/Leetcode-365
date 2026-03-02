from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #bruteforce method is by using a seen set to add node if we have seen it
        #time and space complexity will be O(n)
        # curr = head
        # seen = set()
        # while curr:
        #     if curr in seen:
        #         return True
        #     else:
        #         seen.add(curr)
        #     curr = curr.next
        # return False

        #optimal solution by using slow and fast counter
        #space complexity will be O(1) and time complexity will be O(n)
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False
    
if __name__ == "__main__":
    node = Solution()
    head = ListNode(3)
    a = ListNode(2)
    b = ListNode(0)
    c = ListNode(-4)
    head.next = a
    a.next = b
    b.next = c
    c.next = a

    print(node.hasCycle(head))