class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """

        
        def word_break(s, words):
            is_valid_prefix = lambda word, prefix: word[:len(prefix)] == prefix

            
            memo = {}
            def helper(curr_prefix):
                if curr_prefix in memo:
                    return memo[curr_prefix]
                
                if s == curr_prefix:
                    memo[curr_prefix] = True
                    return True

                for word in words:
                    newprefix = curr_prefix + word
                    if is_valid_prefix(s, newprefix):
                        result = helper(newprefix)
                        if result:
                            memo[curr_prefix] = True
                            return True
                        
                memo[curr_prefix] = False
                return False
                
                
            return helper("")

        return word_break(s, wordDict)

