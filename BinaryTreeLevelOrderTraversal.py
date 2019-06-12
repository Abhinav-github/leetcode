#Given a binary tree, return the level order traversal 
#of its nodes' values. (ie, from left to right, level by level).

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        ret = []
        level = []
        if not root:
            return ret
        ret.append((root,0))
        while ret:
            node, curr_level = ret.pop(0)
            if len(level) == curr_level:
                level.append([node.val])
            else:
                level[curr_level].append(node.val)
            if node.left:
                ret.append((node.left,curr_level+1))
            if node.right:
                ret.append((node.right,curr_level+1))
        return level
