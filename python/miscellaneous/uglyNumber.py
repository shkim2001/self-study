class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if not n: 
            return False
        for k in [2,3,5]:
            while n % k == 0:
                n //= k
        return n == 1