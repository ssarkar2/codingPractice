class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        dig_to_letter = {2:"abc", 3:"def", 4:"ghi", 5:"jkl", 6:"mno", 7:"pqrs", 8:"tuv", 9:"wxyz"}

        def helper(current_state, digits):
            if len(digits) == 0:
                return [current_state]
            first_digit = int(digits[0])
            rest = digits[1:]
            results = []
            for letter in dig_to_letter[first_digit]:
                results += helper(current_state + letter, rest)
            return results
            

        if digits == "":
            return []
        else:
            return helper("", digits)

        
