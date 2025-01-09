# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        from collections import deque

        if root == None:
            return []

        q = deque([root])
        qnext = deque()

        result = []
        curlevel = []
        while True:
            node = q.pop()
            curlevel += [node.val]
            if node.left is not None:
                qnext.appendleft(node.left)
            if node.right is not None:
                qnext.appendleft(node.right)
            if len(q) == 0:
                tmp = q
                q = qnext
                qnext = tmp
                result += [curlevel]
                curlevel = []
            if len(q) == 0 and len(qnext) == 0:
                break
        return result
            

            



