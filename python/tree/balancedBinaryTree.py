# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        
        def areSubTreesBalanced(node, height):
            if not node:
                return 0
            
            left_height = areSubTreesBalanced(node.left, 1 + height)
            right_height = areSubTreesBalanced(node.right, 1 + height)
            
            if abs(left_height - right_height) > 1:
                return float('inf')
            
            return 1 + max(left_height, right_height)
        
        
        return areSubTreesBalanced(root, 0) != float('inf')