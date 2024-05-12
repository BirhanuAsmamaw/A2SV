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
    public TreeNode searchBST(TreeNode root, int val) {

if (root == null) {
            return null;
        }

        // If current node's value matches, return it (the whole subtree rooted here)
        if (root.val == val) {
            return root;
        }

        // Search in appropriate subtree based on comparison
        if (val < root.val) {
            return searchBST(root.left, val); // Search in left subtree
        } else {
            return searchBST(root.right, val); // Search in right subtree
        }
        
    }
}
