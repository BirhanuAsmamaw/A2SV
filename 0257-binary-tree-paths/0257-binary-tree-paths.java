

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode() {}
    TreeNode(int val) { this.val = val; }
    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

class Solution {
    public List<String> binaryTreePaths(TreeNode root) {
        List<String> paths = new ArrayList<>();
        traverse(root, "", paths);
        return paths;
    }

    private void traverse(TreeNode node, String path, List<String> paths) {
        if (node == null) return;
        if (node.left == null && node.right == null) { // leaf node
            paths.add(path + node.val);
            return;
        }
        traverse(node.left, path + node.val + "->", paths);
        traverse(node.right, path + node.val + "->", paths);
    }
}
