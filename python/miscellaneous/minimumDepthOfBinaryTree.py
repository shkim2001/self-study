# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        currentLevel = 0
        if root is None:
            return currentLevel

        queue = deque()
        queue.append(root)

        while queue:
            currentLevel += 1
            for _ in range(len(queue)):
                currentNode = queue.popleft()
                if not currentNode.left and not currentNode.right:
                    return currentLevel
                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)

        return currentLevel