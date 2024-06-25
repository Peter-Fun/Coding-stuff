# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def bstToGst(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        node_sum = [0]  # Using a list to emulate a mutable integer reference
        self.bst_to_gst_helper(root, node_sum)
        return root

    def bst_to_gst_helper(self, root, node_sum):
        # If root is null, make no changes.
        if root is None:
            return

        self.bst_to_gst_helper(root.right, node_sum)
        node_sum[0] += root.val
        # Update the value of root.
        root.val = node_sum[0]
        self.bst_to_gst_helper(root.left, node_sum)
