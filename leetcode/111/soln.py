# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        from collections import deque

        def binary_tree_min_depth(root):
            q = deque([(1,root)])
            cur_level = 0
            while(True):
                lvl, node = q.pop()
                if node.left==None and node.right==None:
                    return lvl
                else:
                    if node.left is not None:
                        q.appendleft((lvl+1, node.left))
                    if node.right is not None:
                        q.appendleft((lvl+1, node.right))
        if root == None:
            return 0
        else:
            return binary_tree_min_depth(root)
