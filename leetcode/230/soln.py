# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        
        def helper(root, k):
            if root == None:
                return None, 0

            value_found, num_elems_l = helper(root.left, k)
            if value_found is not None:
                return value_found, None
            else:
                if k-num_elems_l-1 > 0:
                    value_found, num_elems_r = helper(root.right, k-num_elems_l-1)
                    if value_found is not None:
                        return value_found, None
                    else:
                        return None, num_elems_l + 1 + num_elems_r
                else:
                    return root.val, None

        return helper(root, k)[0]
