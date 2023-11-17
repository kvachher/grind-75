class Solution(object):
    def kthSmallest(self, root, k):
        def inorderTraversal(root):
            res = []
            if root:
                res = inorderTraversal(root.left) 
                res.append(root.val)
                res = res + inorderTraversal(root.right)
            return res
        ans = inorderTraversal(root)
        return ans[k - 1]
