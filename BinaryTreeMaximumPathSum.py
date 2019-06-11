#Given a non-empty binary tree, find the maximum path sum.
#For this problem, a path is defined as any sequence of nodes 
#from some starting node to any node in the tree along the 
#parent-child connections. The path must contain at least one 
#node and does not need to go through the root.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root):
        self.res = -sys.maxsize-1
        self.oneSideSum(root)
        return self.res
    
    # compute one side maximal sum, 
    # (root+left children, or root+right children),
    # root is the included top-most node 
    def oneSideSum(self, root):
        if not root:
            return 0
        left = max(0, self.oneSideSum(root.left))
        right = max(0, self.oneSideSum(root.right))
        self.res = max(self.res, left + right + root.val)
        return max(left, right) + root.val
