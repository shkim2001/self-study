class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        mem = {}
        def fib(n):
            if n <=2:
                return n
            if n not in mem:
                mem[n] = fib(n-1)+fib(n-2)
            return mem[n]
        return fib(n)