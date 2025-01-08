class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[i][j] = None
        
        # zero out rows
        for i in range(m):
            zero_out_row = False
            for j in range(n):
                if matrix[i][j] == None:
                    zero_out_row = True
                    break
            if zero_out_row:
                for j in range(n):
                    if matrix[i][j] != None:
                        matrix[i][j] = 0
        
        # zero out cols
        for j in range(n):
            zero_out_col = False
            for i in range(m):
                if matrix[i][j] == None:
                    zero_out_col = True
                    break
            if zero_out_col:
                for i in range(m):
                    if matrix[i][j] != None:
                        matrix[i][j] = 0

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == None:
                        matrix[i][j] = 0

