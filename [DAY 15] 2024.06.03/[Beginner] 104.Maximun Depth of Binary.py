# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
깊이우선탐색(DFS)

[]
[(3,1)]
[(9,2), (20,2)]
[(9,2), (15,3), (7,3)]
[(9,2), (15,3)]
[(9,2), (4,4)]
[(9,2)]
[]
'''

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        max_depth = 0
        my_stack = [(root,1)]
        while my_stack:
            node,depth = my_stack.pop()
            max_depth = max(depth,max_depth)
            if node.left:
                my_stack.append((node.left,depth+1))
            if node.right:
                my_stack.append((node.right,depth+1))
        return max_depth

"""
재귀
    3(4)
   /    \
 9(1)  20(3)
       /  \
    15(2) 7(1)
     /
  4(1)
"""

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        # else:
        #     left_d = self.maxDepth(root.left)
        #     right_d = self.maxDepth(root.right)
        # return max(left_d, right_d) +1

        return 1 + max(
            self.maxDepth(root.left),
            self.maxDepth(root.right)
        )