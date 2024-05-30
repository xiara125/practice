# Runtime 114ms

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        stack = [root]        
        range_sum = 0
        
        while stack:
            node = stack.pop()
            
            if node:
                if low < node.val:
                    stack.append(node.left)
                
                if node.val < high:
                    stack.append(node.right)
                
                if low <= node.val <= high:
                        range_sum += node.val
                        
        return range_sum