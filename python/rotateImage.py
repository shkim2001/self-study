class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        j = 0
        for i in zip(*matrix):
            matrix[j] = i[::-1]
            j+=1