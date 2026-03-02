from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #create a dummy node to start updating
        #have a carry to store overflow of addition
        #loop through the given nodes
        carry = 0
        dummy = ListNode(0)
        tail = dummy

        while l1 or l2 or carry:    
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry = total // 10
            digit = total % 10

            tail.next = ListNode(digit)
            tail = tail.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy.next

def print_linked_list(head: Optional[ListNode]) -> None:
    values = []
    curr = head
    while curr:
        values.append(str(curr.val))
        curr = curr.next
    print(" -> ".join(values) if values else "Empty")

if __name__ =="__main__":
    l1 = ListNode(2)
    a1 = ListNode(4)
    a2 = ListNode(3)
    l1.next = a1
    a1.next = a2

    l2 = ListNode(5)
    b1 = ListNode(6)
    b2 = ListNode(4)
    l2.next = b1
    b1.next = b2

    add = Solution()
    result = add.addTwoNumbers(l1, l2)
    print_linked_list(result)
