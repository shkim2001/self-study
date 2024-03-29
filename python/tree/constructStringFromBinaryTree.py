# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def dfs(root):
            if not root:
                return ""
            
            left = dfs(root.left)
            right = dfs(root.right)
            
            if left is "" and right is "":
                return str(root.val)
            elif right is "":
                return str(root.val) + "(" + left + ")"
            else:
                return str(root.val) + "(" + left + ")"+ "(" + right + ")"
        
        return dfs(root)