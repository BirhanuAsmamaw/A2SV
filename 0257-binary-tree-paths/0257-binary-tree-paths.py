# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []
        def dfs(node,path):
            if not node.right and not node.left:
                path.append(str(node.val))
                ans.append(path.copy())
                path.pop()
                return
            
            path.append(str(node.val))
            if node.left:
                dfs(node.left,path)
            if node.right:
                dfs(node.right,path)
            path.pop()
            
        dfs(root,[])
        for i in range(len(ans)):
            ans[i] = "->".join(ans[i])

        return ans

            
