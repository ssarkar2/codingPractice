class Solution(object):
    def lengthOfLIS(self, nums):
        memo = {0:1}
        def helper(i):
            if i in memo:
                return memo[i]

            lst = []
            for k in range(i):
                x = helper(k)
                if nums[k] < nums[i]:
                    lst += [1+x]
            if len(lst) > 0:
                val = max(lst)
            else:
                val = 1
            memo[i] = val
            return val  
        
        if len(nums) == 0:
            return 0
        out = helper(len(nums)-1)
        return max(memo.values())
