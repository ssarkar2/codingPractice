class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        memo = {}

        def helper(last_robbed, sum_till_now, considering_robbing_next):
            #print(last_robbed, sum_till_now, considering_robbing_next, '...')
            #basecase
            if (last_robbed, sum_till_now, considering_robbing_next) in memo:
                return memo[(last_robbed, sum_till_now, considering_robbing_next)]
            if considering_robbing_next == len(nums):
                memo[(last_robbed, sum_till_now, considering_robbing_next)] = sum_till_now
                return sum_till_now


            # dont rob considering_robbing_next
            val = sum_till_now + helper(last_robbed, 0, considering_robbing_next+1)
            if considering_robbing_next-last_robbed > 1 or last_robbed==-1:
                # rob considering_robbing_next
                val2 = sum_till_now + helper(considering_robbing_next, nums[considering_robbing_next], considering_robbing_next+1)
                #print('rob', considering_robbing_next)
                if val2 > val:
                    val = val2
            #print(last_robbed, sum_till_now, considering_robbing_next, val)
            memo[(last_robbed, sum_till_now, considering_robbing_next)] = val
            return val

        return helper(-1, 0, 0)

