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
    
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #create a dummy node to facilitate adding nodes
        dummy = ListNode(0)
        tail = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        tail.next = list1 if list1 else list2
        return dummy.next
    

    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        #will do this in 3 steps
        #step 1: do the first phased to get the len of the linked list
        #step 2: get the n - k nodes at the end of the list
        #step 3 connect the k nodes to the start of the list
        if not head or not head.next or k == 0:
            return head

        #step 1, get the tail of the list
        n = 1
        tail = head
        while tail.next:
            tail = tail.next
            n += 1
        
        #avoid unnecesary rotations for k > n
        k %= n
        if k == 0:
            return head

        #create the circle
        tail.next = head

        #step 2, and get the next tail
        new_tail = head
        for _ in range(n- k - 1):
            new_tail = new_tail.next

        new_head = new_tail.next
        new_tail.next = None

        return new_head
    
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        #use two linked lists, one for less than and the other one for greater than x nodes
        #at the end we connect them

        #creating dummy nodes to help in connecting
        less_dummy = ListNode(0)
        greater_dummy = ListNode(0)
        less_tail = less_dummy
        greater_tail = greater_dummy

        #iterate through the given 
        cur = head
        while cur:
            #get the next node after current, detach the nodes
            nxt = cur.next
            cur.next = None

            #add the necessary nodes to their nodes
            if cur.val < x:
                less_tail.next = cur
                less_tail = less_tail.next
            else:
                greater_tail.next = cur
                greater_tail = greater_tail.next
            cur = nxt
        
        #connect the two lists
        less_tail.next = greater_dummy.next

        return less_dummy.next
        


def print_linked_list(head: Optional[ListNode]) -> None:
    values = []
    curr = head
    while curr:
        values.append(str(curr.val))
        curr = curr.next
    print(" -> ".join(values) if values else "Empty")

if __name__ =="__main__":
    # Inputs for addTwoNumbers (digits are in reverse order).
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))

    # Inputs for mergeTwoLists must be sorted.
    m1 = ListNode(1, ListNode(2, ListNode(4)))
    m2 = ListNode(1, ListNode(3, ListNode(4)))

    #input for rotate list
    r1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(2))))))

    #input for partition list
    p1 = ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(7, ListNode(5, ListNode(2)))))))

    linked_list = Solution()
    sum_result = linked_list.addTwoNumbers(l1, l2)
    merge_result = linked_list.mergeTwoLists(m1, m2)
    rotate_list = linked_list.rotateRight(r1, 2)
    partition = linked_list.partition(p1, 3)

    print("addTwoNumbers:")
    print_linked_list(sum_result)
    print("mergeTwoLists:")
    print_linked_list(merge_result)
    print("rotateList:")
    print_linked_list(rotate_list)
    print("Partition:")
    print_linked_list(partition)

