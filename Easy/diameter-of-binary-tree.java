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
    public int diameterOfBinaryTree(TreeNode root) {
        int diameter[] = new int [1];

        recurse(root, diameter);

        return diameter[0];
    }

    public int recurse(TreeNode root, int d[]) {
        if (root == null)
            return 0;
        int l = recurse(root.left, d);
        int r = recurse(root.right, d);

        d[0] = Math.max(d[0], l + r);

        return Math.max(l, r) + 1; 
    }
}
