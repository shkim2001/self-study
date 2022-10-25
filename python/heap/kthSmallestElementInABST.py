# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from heapq import *
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        minHeap = []
        queue = collections.deque()
        if root:
            queue.append(root)
        
        while queue:
            for i in range(len(queue)):
                currentNode = queue.popleft()
                heappush(minHeap, currentNode.val)
                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)
            
        for i in range(k):
            result = heappop(minHeap)
        
        return result