class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        def is_pal(word):
            for i in range(len(word)//2):
                if word[i] != word[len(word)-1-i]:
                    return False
            return True


        '''
        state is partitioning of prev letters, letters is remaining letters to partition
        '''
        def helper(state, letters):
            if len(letters) == 0:
                return [state]
            final = []
            for i in range(1,len(letters)+1):
                cur_prefix = letters[:i]
                rest = letters[i:]
                if is_pal(cur_prefix):
                    final += helper(state + [cur_prefix], rest)
            return final

            

        return helper([], s)
