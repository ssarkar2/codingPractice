#https://www.hackerrank.com/challenges/tree-top-view/problem
"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)"""

def helper(root, flag):
    if root is None:
        return
    if flag == 0: #the actual root
        helper(root.left, 1)
        print root.data,
        helper(root.right, 2)
    else:
        if flag==1:
            helper(root.left, 1)
            print root.data,
        else:
            print root.data,
            helper(root.right, 2)
        
    

def topView(root):
    helper(root, 0)
