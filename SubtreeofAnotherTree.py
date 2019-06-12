# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s: 
            return False
        if self.equal(s, t): 
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def equal(self, p: TreeNode, q: TreeNode) -> bool:
        if p and q:
            return p.val == q.val and self.equal(p.left, q.left) and self.equal(p.right, q.right)
        return p is q
