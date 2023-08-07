# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        m = 0

        while root:
            if not root.left:
                m += root.val
                root = root.right

                if not root and m == targetSum:
                    return True
            else:
                prev = root.left
                n = prev.val

                while prev.right and prev.right != root:
                    prev = prev.right
                    n += prev.val

                if not prev.right:
                    m += root.val
                    prev.right = root

                    if not prev.left and m + n == targetSum:
                        return True

                    root = root.left
                else:
                    prev.right = None
                    root = root.right
                    m -= n

        return False