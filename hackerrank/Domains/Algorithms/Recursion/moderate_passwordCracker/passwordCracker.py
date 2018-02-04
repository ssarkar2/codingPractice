#!/bin/python
#https://www.hackerrank.com/challenges/password-cracker/problem
import sys, pdb
sys.setrecursionlimit(15000)
tbl = {}
def passwordCracker(passwords, attempt):
    #print attempt, len(attempt)
    #pdb.set_trace()
    if len(attempt)==0:
        return ([], True)
    possibilities = []
    for pwd in passwords:
        if pwd == attempt[:len(pwd)]:
            possibilities += [pwd]
    possibilities.sort(lambda x,y: cmp(-len(x), -len(y)))
    for pwd in possibilities:
        key = attempt[len(pwd):]
        if key in tbl:
            lst, flag = tbl[key]
        else:
            lst, flag = passwordCracker(passwords, attempt[len(pwd):])
            tbl[key] = (lst, flag)
        if flag:
            return ([pwd] + lst, True)
    return ([], False)

if __name__ == "__main__":
    
    t = int(raw_input().strip())
    for a0 in xrange(t):
        n = int(raw_input().strip())
        password = raw_input().strip().split(' ')
        attempt = raw_input().strip()
        result = passwordCracker(password, attempt)
        print ' '.join(result[0]) if result[1] else 'WRONG PASSWORD'
        tbl = {}
    '''
    
    #result = passwordCracker(['because', 'can', 'do', 'must', 'we', 'what'], 'wedowhatwemustbecausewecan')
    #print ' '.join(result[0]) if result[1] else 'WRONG PASSWORD'
    
    pwds = ['a', 'aa', 'aaa', 'aaaa', 'aaaaa', 'aaaaaa', 'aaaaaaa', 'aaaaaaaa', 'aaaaaaaaa', 'aaaaaaaaaa']
    query = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab'
    result = passwordCracker(pwds, query)
    print ' '.join(result[0]) if result[1] else 'WRONG PASSWORD'
    '''
