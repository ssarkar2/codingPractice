class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        numones = 0
        val = n
        while(True):
            if val%2 == 1:
                numones += 1
            val = val // 2
            if val == 0:
                break
        return numones
