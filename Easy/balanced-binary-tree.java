/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public boolean isBalanced(TreeNode root) {
        if (root == null)
            return true;
        int depth1 = 0; 
        int depth2 = 0;
        if (root.left != null) 
            depth1 = helper(root.left);
        if (root.right != null)
            depth2 = helper(root.right);
        System.out.println("The left depth is: " + depth1);
        System.out.println("The right depth is: " + depth2);
        return (Math.abs(depth1 - depth2) < 2) && (isBalanced(root.left) && isBalanced(root.right)); 
    }
    public int helper(TreeNode root) {
        if (root == null)
            return 0;

        int leftDepth = helper(root.left);
        int rightDepth = helper(root.right);

        return 
            Math.max(leftDepth, rightDepth) + 1;
    }
}
