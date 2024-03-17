# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        linked = ListNode()
        current = linked
        pointer = 0

        while l1 or l2 or pointer:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            
            new_val = v1 + v2 + pointer
            pointer = new_val // 10
            new_val = new_val % 10
            current.next = ListNode(new_val)
            
            current = current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return linked.next
        
        
