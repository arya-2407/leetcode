class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            #base case
            if not root:
                return [True,0]
                
            # idea is that tree is balanced when:
            #  1.when the heights of lChild and rChild are lesser than 1
            #  2. lChild and rChild trees are balanced themselves
            left = dfs(root.left)
            right = dfs(root.right)
            balanced = (left[0] and right[0] and 
                        abs(left[1] - right[1]) <= 1)
            return [balanced,1+max(left[1],right[1])]
        return dfs(root)[0]