class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root:
            return []
        
        left_tree = self.inorderTraversal(root.left)
        right_tree = self.inorderTraversal(root.right)
        
        return left_tree + [root.val] + right_tree