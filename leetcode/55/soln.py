class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if False:
            memo = {}
            def helper(currloc):
                if currloc in memo:
                    return memo[currloc]
                if currloc == len(nums)-1:
                    return True
                else:
                    for i in range(1,nums[currloc]+1):
                        retval = helper(currloc+i)
                        if retval:
                            memo[currloc] = True
                            return True
                    memo[currloc] = False
                    return False
            return helper(0)
        elif False:
            reachability = [False] * len(nums)
            reachability[-1] = True
            for i in range(len(nums)-1, -1, -1):
                curr_val = nums[i]
                for j in range(1, curr_val+1):
                    #print(i,j)
                    if i+j >= len(nums):
                        break
                    if reachability[i+j]:
                        reachability[i] = True
                        break
            return reachability[0]
        elif False:

            from collections import deque

            q = deque([0])
            memo = {}
            while len(q) > 0:
                idx = q.pop()
                if idx == len(nums)-1:
                    #memo[idx] = True
                    return True
                if idx > len(nums)-1:
                    idx = len(nums)-1
                for i in range(1, nums[idx]+1):
                    q.append(idx+i)
            return False
        else:
            goal = len(nums)-1
            for i in range(len(nums)-2, -1, -1):
                curval = nums[i]
                if curval >= goal-i:
                    goal = i
            return goal==0
