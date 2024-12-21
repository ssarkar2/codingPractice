class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(intervals)==0:
            return []
        intervals = sorted(intervals, key=lambda x:x[0])
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            curr = intervals[i]
            if curr[0] <= res[-1][1]:
                res[-1][1] = max(res[-1][1], curr[1])
            else:
                res += [curr]
        return res
        
