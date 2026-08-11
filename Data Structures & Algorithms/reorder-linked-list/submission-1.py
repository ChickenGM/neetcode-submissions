# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def reverseList(head: [ListNode]):
    curr = head
    prev = None
    while curr is not None:
        nextNode = curr.next
        curr.next = prev

        prev = curr
        curr = nextNode

    return prev


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
        second = slow.next
        prev = slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        first, second = head, prev
        while second:
            temp_1, temp_2 = first.next, second.next
            first.next = second
            second.next = temp_1
            first, second = temp_1, temp_2

        

        
        
        