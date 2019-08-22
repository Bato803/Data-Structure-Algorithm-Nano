# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if root.val==key:
            newVal = self.findNxtLargest(root.right)
            root.val = newVal
            return

        if root.val>key:
            self.deleteNode(root.left, key)
        elif root.val<key:
            self.deleteNode(root.right, key)

        return root

    def findNxtLargest(self, root):
        if not root.left:
            val = root.val
            root.val = None
            return val
        self.findNxtLargest(self, root.left)
