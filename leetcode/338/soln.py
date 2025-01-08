class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """

        if n == 0:
            return [0]
        if n == 1:
            return [0,1]
        res = [0,1] + [None] * (n-1)

        num_bin = 1
        idx = 1
        xt = False
        while(True):
            num_bin += 1
            # need to fill 2^(num_bin-1) -> 2^num_bin]
            base = 2**(num_bin-1)
            for i in range(2**(num_bin-1)):
                idx += 1
                if idx == (n+1):
                    xt = True
                    break 
                res[base + i] = 1 + res[i]
            if xt:
                break
        return res
