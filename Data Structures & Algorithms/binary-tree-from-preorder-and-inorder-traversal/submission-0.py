# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        seen = {}
        for i, num in enumerate(inorder):
            seen[num] = i
        self.pre_idx = 0
        
        def dfs(l, r):
            if l > r:
                return None

            val = preorder[self.pre_idx]
            node = TreeNode(val)
            self.pre_idx += 1

            rootIdx = seen[val]

            node.left = dfs(l, rootIdx - 1)
            node.right = dfs(rootIdx + 1, r)

            return node

        return dfs(0, len(preorder) - 1)

