class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        def helper(state, t):
            if t == target:
                return [state]

            final = []
            for i in candidates:
                if t+i <= target:
                    final += helper(state + [i], t+i)
            return final

        x = helper([], 0)
        hist_list = []
        for idx in range(len(x)):
            hist = {}
            for item in x[idx]:
                hist[item] = hist.get(item,0) + 1
            hist_list += [hist]

        final = []
        for k in hist_list:
            if k not in final:
                final += [k]
        
        return [sum([[k]*i[k] for k in i],[]) for i in final]

