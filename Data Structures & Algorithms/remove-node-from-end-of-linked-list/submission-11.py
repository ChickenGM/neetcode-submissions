# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # brute-force
        storing = []
        cur = head
        while cur:
            storing.append(cur)
            cur = cur.next
        removeIndex = len(storing) - n
        if removeIndex == 0:
            return head.next
        storing[removeIndex - 1].next = storing[removeIndex].next
        return head



        
        