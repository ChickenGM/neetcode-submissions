# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        check = set()
        curr = head
        while curr:
            temp = curr.next
            if curr not in check:
                check.add(curr)
            else:
                return True
            curr = temp
        return False
    
         
        