class Solution(object):
    def isValidBST(self, root):
        def inorderTraversal(root):
            res = []
            if root:
                res = inorderTraversal(root.left) 
                res.append(root.val)
                res = res + inorderTraversal(root.right)
            return res
        ans = inorderTraversal(root)
        for i in range(1, len(ans)) : 
            if ans[i - 1] >= ans[i] : 
                return False
        return True
