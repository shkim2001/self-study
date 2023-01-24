class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        count = Counter(s+t)
        for k, v in count.items():
            if v % 2 == 1:
                return k
        return None