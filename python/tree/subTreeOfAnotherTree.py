# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        
        if self.isSameTree(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
    
    def isSameTree(self, root:Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
            if not subRoot and not root:
                return True
            elif subRoot and root and subRoot.val == root.val:
                return self.isSameTree(root.left, subRoot.left) and self.isSameTree(root.right, subRoot.right)
            return False