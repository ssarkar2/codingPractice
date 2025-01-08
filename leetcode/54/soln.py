class Index:
    def __init__(self, r, c):
        self.idx = (0,0)
        self.dir = (0,1)
        self.r = r
        self.c = c
        self.r_upper = 0
        self.r_lower = r
        self.c_left = -1
        self.c_right = c
    
    def check(self):
        assert self.idx[0] >= 0
        assert self.idx[0] < self.r
        assert self.idx[1] >= 0
        assert self.idx[1] < self.c
        # exactly 1 zero
        assert ((0,1)[self.dir[0]==0] + (0,1)[self.dir[1]==0]) == 1

    def inc(self):
        #self.check() 
        #print('inc', self.idx, self.dir)
        possible_val = (self.idx[0]+self.dir[0], self.idx[1]+self.dir[1])
        if possible_val[1] == self.c_right and self.dir == (0,1):
            #print('bump1')
            #assert self.dir == (0,1)
            self.dir = (1,0)
            self.c_right -= 1
            return self.inc()
        if possible_val[0] == self.r_lower and self.dir == (1,0):
            #print('bump2')
            #assert self.dir == (1,0)
            self.dir = (0,-1)
            self.r_lower -= 1
            return self.inc()
        if possible_val[1] == self.c_left and self.dir == (0,-1):
            #print('bump3')
            #assert self.dir == (0,-1)
            self.dir = (-1,0)
            self.c_left += 1
            return self.inc()
        if possible_val[0] == self.r_upper and self.dir == (-1,0):
            #print('bump4')
            #assert self.dir == (-1,0)
            self.dir = (0,1)
            self.r_upper += 1
            return self.inc()
        #print(self.idx)
        self.idx = possible_val
        #print(self.idx, self.dir, '..')
        #self.check()
        return self.idx

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        r = len(matrix)
        c = len(matrix[0])
        if r == 1 and c == 1:
            return [matrix[0][0]]
        if r == 1:
            return matrix[0]
        if c == 1:
            return [row[0] for row in matrix]
        idx = Index(r, c)
        res = []
        for i in range(r*c):
            res += [matrix[idx.idx[0]][idx.idx[1]]]
            idx.inc()
        return res

