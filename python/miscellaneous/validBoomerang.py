class Solution(object):
    def isBoomerang(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        points_set = set()
        for x,y in points:
            points_set.add((x,y))
        if len(points_set) < 3:
            return False
        points.sort()
        x1,y1 = points[0]
        x2,y2 = points[1]
        x3,y3 = points[2]
        return not((x2-x1)*(y3-y2) == (x3-x2)*(y2-y1))