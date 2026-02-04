# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # traverse the bst
        arr = []
        numsToSum = []
        total = 0
        
        def inOrderTraversal(root):
            if root is None:
                return
            
            inOrderTraversal(root.left)
            arr.append(root.val)
            inOrderTraversal(root.right)
        
        inOrderTraversal(root)
        
        for num in arr:
            if low <= num <= high:
                numsToSum.append(num)
                total = sum(numsToSum)
        
        return total