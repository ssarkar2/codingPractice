#!/bin/python
#https://www.hackerrank.com/challenges/crossword-puzzle/problem
import sys, pdb

def findslots(board_): #assumes two words touch at right angles only
    #newboard = [k for k in board] #a copy
    slots = []
    board = [[i for i in r] for r in board_] #a copy
    for ridx, r in enumerate(board):
        for cidx, item in enumerate(r):
            if item == '-':                
                if ridx+1>=10:
                    coltype = False
                else:
                    coltype = board[ridx+1][cidx] == '-'
                if cidx+1>=10:
                    rowtype = False
                else:
                    rowtype = board[ridx][cidx+1] == '-'
                if coltype:
                    explore_next_row = 1
                    while(True):
                        if ridx+explore_next_row >= 10:
                            break
                        if board[ridx+explore_next_row][cidx]=='+':
                            break
                        else:
                            if cidx==9 or board[ridx+explore_next_row][cidx+1] is not '-':
                                if cidx==0 or (cidx > 0 and board[ridx+explore_next_row][cidx-1] is not '-'):
                                    board[ridx+explore_next_row][cidx] = '+'
                        explore_next_row += 1
                    slots += [(ridx, cidx, explore_next_row, 'D')]
                if rowtype:
                    #if ridx==6 and cidx==4:
                    #    pdb.set_trace()
                    explore_next_col = 1
                    while(True):
                        if cidx+explore_next_col >= 10:
                            break
                        if board[ridx][cidx+explore_next_col]=='+':
                            break
                        else:
                            if ridx==9 or board[ridx+1][cidx+explore_next_col] is not '-':
                                if ridx==9 or (ridx < 9 and board[ridx+1][cidx+explore_next_col] is not '-'):
                                    board[ridx][cidx+explore_next_col] = '+'
                        explore_next_col += 1
                    slots += [(ridx, cidx, explore_next_col, 'A')]
                board[ridx][cidx] = '+'
    #print slots, 'in findslots'
    return slots
           
def printboard(board):
    print '###########'
    for r in board:
        print ''.join(r)
    print '-------'

def fillword(board, word, slot):
    startr = slot[0]
    startc = slot[1]
    newboard = [[i for i in r] for r in board]
    for idx, letter in enumerate(word): 
        if slot[-1] == 'D':
            #print idx, letter, 'D', startr, startc, newboard[startr][startc], newboard[startr+1][startc]
            newboard[startr+idx][startc] = letter
        else:
            newboard[startr][startc+idx] = letter
        #printboard(newboard); print 'ddd', word
    return newboard

def getPossibleSlots(board, slots, currword):
    possibleslots = [(i,s) for i,s in enumerate(slots) if len(currword)==s[2]]
    possibleslotsnew = []
    for ii,ps in possibleslots:
        if ps[-1] == 'D':
            curroccupant = [board[ps[0]+i][ps[1]] for i in range(ps[2])]
        else:
            curroccupant = [board[ps[0]][ps[1]+i] for i in range(ps[2])]
        #check compatibility of current occupant and currword                
        compat = all([currocc=='-' or currocc==currwordch for currocc, currwordch in zip(curroccupant,currword)])
        if compat:
            possibleslotsnew += [(ii,ps)]
    #print possibleslotsnew, 'eeeee'
    #printboard(board)
    return possibleslotsnew

def helper(board, hintlist, slots):
    #print 'enter helper', hintlist
    #if len(hintlist)==0:
    #    return (board, True)
    
    if len(slots) == 0:
        return (board, True)
    currword = hintlist[0]
    #possibleslots = [s for s in slots if len(currword)==s[2]]
    possibleslots = getPossibleSlots(board, slots, currword)
    boardorig = [[i for i in r] for r in board]
    #print currword, possibleslots
    if len(possibleslots) == 0:
        #pdb.set_trace()
        return (board, False)
    #printboard(boardorig)
    for slotsidx, s in possibleslots:
        board = fillword(boardorig, currword, s)
        #printboard(board); print hintlist[1:]
        board, flag = helper(board, hintlist[1:], [slots[kk] for kk in range(len(slots)) if kk != slotsidx])
        if flag:
            return (board, True)
    return (boardorig, False)

def crosswordPuzzle(crossword, hints):
    # Complete this function
    #for r in crossword:
    #    print r
    emptyboard = [[i for i in r] for r in crossword]
    #printboard(emptyboard)
    slots = findslots(emptyboard)
    hintlist = hints.split(';')
    #printboard(emptyboard)
    #print slots, len(slots), len(hintlist)
    assert len(slots) == len(hintlist)
    board, flag = helper(emptyboard, hintlist, slots)
    #print board
    
    return [''.join(r) for r in board]

if __name__ == "__main__":
    '''
    crossword = []
    crossword_i = 0
    for crossword_i in xrange(10):
        crossword_t = str(raw_input().strip())
        crossword.append(crossword_t)
    hints = raw_input().strip()
    result = crosswordPuzzle(crossword, hints)
    print "\n".join(map(str, result))
    '''
    
    
    hints = 'AGRA;NORWAY;ENGLAND;GWALIOR'
    crossword = ['+-++++++++',
                 '+-++++++++',
                 '+-------++',
                 '+-++++++++',
                 '+-++++++++',
                 '+------+++',
                 '+-+++-++++',
                 '+++++-++++',
                 '+++++-++++',
                 '++++++++++']
    result = crosswordPuzzle(crossword, hints)
    print "\n".join(map(str, result))
    
    hints = 'CALIFORNIA;NIGERIA;CANADA;TELAVIV'
    crossword = ['+-++++++++',
                 '+-++-+++++',
                 '+-------++',
                 '+-++-+++++',
                 '+-++-+++++',
                 '+-++-+++++',
                 '++++-+++++',
                 '++++-+++++',
                 '++++++++++',
                 '----------']
    result = crosswordPuzzle(crossword, hints)
    print "\n".join(map(str, result))
    
    
    hints = 'ANDAMAN;MANIPUR;ICELAND;ALLEPY;YANGON;PUNE'
    crossword = ['+-++++++++',
                 '+-------++',
                 '+-++-+++++',
                 '+-------++',
                 '+-++-++++-',
                 '+-++-++++-',
                 '+-++------',
                 '+++++++++-',
                 '++++++++++',
                 '++++++++++']
    result = crosswordPuzzle(crossword, hints)
    print "\n".join(map(str, result))
                 