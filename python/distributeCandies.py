class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        sortedCandy = set(candyType)
        
        if len(candyType) // 2 >= len(sortedCandy):
            return len(sortedCandy)
        
        return len(candyType) // 2
