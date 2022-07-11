class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        if len(s) != len(goal):
                return False
        if len(s) == 0:
                return True

        for index in xrange(len(s)):
            if all(s[(index+i) % len(s)] == goal[i] for i in xrange(len(s))):
                return True
        return False   