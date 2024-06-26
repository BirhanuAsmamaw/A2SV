# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None
        root = TreeNode(preorder[0])
        def bfs(root,current):
            if current < root.val:
                if root.left == None:
                    root.left = TreeNode(current)
                bfs(root.left,current)
            elif current > root.val:
                if root.right == None:
                    root.right  = TreeNode(current)

                bfs(root.right,current)
    
        for value in preorder[1:]:
            bfs(root,value)  
        return root
