# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head: return False
        if not head.next:
            return False
        if not head.next.next:
            return False
        slow , fast = head, head
        while fast:
            if fast.next:
                temp_s = slow.next
                temp_f = fast.next.next
            else:
                return False
            if temp_s == temp_f:
                return True
            else:
                slow = temp_s
                fast = temp_f
        return False
    
         
        