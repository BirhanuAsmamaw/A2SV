# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        final = ListNode()
        
        final.next = head
        current = final
        
        while current:
            if current.next and current.next.next and current.next.val == current.next.next.val:
                temp = current.next.next
                while temp and temp.next and temp.val == temp.next.val:
                    temp = temp.next
                current.next = temp.next
                    
            else:
                current = current.next
        return final.next
        