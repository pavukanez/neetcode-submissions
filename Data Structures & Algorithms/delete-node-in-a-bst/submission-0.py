# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # root has 0 or 1 child
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            
            # root has 2 children
            cur = root.right
            while cur.left:
                cur = cur.left
            
            root.val = cur.val

            root.right = self.deleteNode(root.right, cur.val)
        
        return root