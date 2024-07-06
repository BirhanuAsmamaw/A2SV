/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public boolean isPalindrome(ListNode head) {
        List<Integer> result = new ArrayList<>();
        ListNode n = head;
        while (n != null) {
            result.add(n.val);
            n = n.next;
        }
        
        int start = 0;
        int end = result.size() - 1;
        while (start < end) {
            if (!result.get(start).equals(result.get(end))) {
                return false;
            }
            start++;
            end--;
        }
        
        return true;
        
    }
}
