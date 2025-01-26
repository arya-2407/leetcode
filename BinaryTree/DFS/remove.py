# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):

        """
        :type root: Optional[TreeNode]
        :type key: int
        :rtype: Optional[TreeNode]
        """

        def findMin(root):
            cur = root
            while cur and cur.left:
                cur = cur.left
            return cur
        
        if not root:
            return None
        
        #search key
        if key > root.val:
            root.right = self.deleteNode(root.right,key)
        elif key < root.val:
            root.left = self.deleteNode(root.left,key)
        else:
            #case #1 : 0 or 1 children
            if not root.right:
                return root.left
            elif not root.left:
                return root.right
            
            #case 2 : 2 children
            else:
                minNode = findMin(root.right)
                root.val = minNode.val
                root.right = self.deleteNode(root.right,minNode.val)
        
        return root
