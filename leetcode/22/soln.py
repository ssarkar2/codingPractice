class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        '''
        n = 4
        state: (()(
        curr_opens  = 2
        num_opens_left = 1
        num_closes_left = 3
        '''
        def helper(state, curr_opens, num_opens_left, num_closes_left):
            if num_opens_left == 0 and num_closes_left == 0:
                return [state]
            
            final = []
            if num_opens_left > 0:
                final += helper(state + '(', curr_opens+1, num_opens_left-1, num_closes_left)
            if curr_opens > 0:
                final += helper(state + ')', curr_opens-1, num_opens_left, num_closes_left-1)
            return final
                

        return helper("", 0, n, n)
