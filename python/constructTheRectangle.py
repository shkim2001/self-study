class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        j = 1
        while j*j <= area:
            if not(area % j):
                L, W = area//j, j
            j += 1
        return [L, W]