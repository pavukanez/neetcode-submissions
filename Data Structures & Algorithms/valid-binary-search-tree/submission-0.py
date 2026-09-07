# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root, minV, maxV):
            if not root:
                return True
            
            if root.val <= minV or root.val >= maxV:
                return False

            return dfs(root.left, minV, root.val) and dfs(root.right, root.val, maxV)

        return dfs(root, -math.inf, math.inf)