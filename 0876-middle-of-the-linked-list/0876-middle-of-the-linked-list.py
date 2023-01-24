# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        leng = 0
        while current != None:
            leng += 1
            current = current.next
        for i in range(leng//2):
            head = head.next
        return head
        
            
            
        