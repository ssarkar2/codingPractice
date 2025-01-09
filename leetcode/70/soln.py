class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo = {}
        def helper(steps):
            if steps in memo:
                return memo[steps]
            if steps == 0:
                return 1
            if steps == 1:
                return 1
            x = helper(steps-1)+helper(steps-2) 
            memo[steps] = x
            return x
        return helper(n)
