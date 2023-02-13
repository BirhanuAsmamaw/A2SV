# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        result = []
        n = head
        while(n):
            result.append(n.val)
            n = n.next
        return result == result[::-1]
        