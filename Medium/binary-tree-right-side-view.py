# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# recursively call node by node
# start by checking if root node exists, if so, add it
# -> for each node, check if the right side exists. if so, recursively call
# -> on right side. else call it on left node.

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def recurse(curr, d, l):
            # if bottom of tree
            if curr is None : 
                return l

            # if depth = length of view, append value
            if d == len(l) : 
                l.append(curr.val)
            
            # right subtree first, then left
            recurse(curr.right, d + 1, l)
            recurse(curr.left, d + 1, l)
            
        ans = []
        recurse(root, 0, ans)
        return ans
