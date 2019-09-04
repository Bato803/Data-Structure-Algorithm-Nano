# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        self.helper(root, res, 0)
        return res

    def helper(self, root, res, level):

        if not root:
            return

        if level>=len(res):
            res.append([])

        res[level].append(root.val)

        self.helper(root.left, res, level+1)
        self.helper(root.right, res, level+1)
