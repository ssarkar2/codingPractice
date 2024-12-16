class Solution(object):
    def row_validator(self, board):
        for row in board:
            rowset = set([])
            for i in row:
                if i != '.':
                    if i in rowset:
                        return False
                    else:
                        rowset.add(i)
        return True
    def col_validator(self, board):
        # col_validator could be implemented in terms of row_validator by transposing
        for colid in range(len(board)):
            colset = set([])
            for rowid in range(len(board)):
                if board[rowid][colid] != '.':
                    if board[rowid][colid] in colset:
                        return False
                    else:
                        colset.add(board[rowid][colid])
        return True

    def cell_validator(self, board):
        for cellrow in range(3):
            for cellcol in range(3):
                relevantrows = board[cellrow*3 : (cellrow+1)*3]
                cell = sum([row[cellcol*3 : (cellcol+1)*3] for row in relevantrows],[])
                # DRY code for this uniqueness search
                cellset = set([])
                for i in cell:
                    if i != '.':
                        if i in cellset:
                            return False
                        else:
                            cellset.add(i)
        return True

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        return self.row_validator(board) and self.col_validator(board) and self.cell_validator(board)
        
