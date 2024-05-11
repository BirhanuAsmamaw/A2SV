# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0
        current = head
        while current != None:
            current = current.next
            length += 1
        for i in range(length // 2):
            head = head.next
            
        return head
        
            
            
        
