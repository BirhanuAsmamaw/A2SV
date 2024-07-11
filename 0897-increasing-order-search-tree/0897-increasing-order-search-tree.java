/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public TreeNode increasingBST(TreeNode root) {
        
        TreeNode node = root;
        Stack<TreeNode> stack = new Stack<>();
        TreeNode pre = null;
        TreeNode smallest = null;
        
        while (!stack.isEmpty() || node != null) {
            if (node != null) {
                stack.push(node);
                node = node.left;
            } else {
                node = stack.pop();
                if (smallest == null) {
                    smallest = node;
                }
                node.left = null;
                if (pre != null) {
                    pre.right = node;
                }
                pre = node;
                node = node.right;
            }
        }
        
        return smallest;
    }
}
