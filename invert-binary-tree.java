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
    public TreeNode invertTree(TreeNode root) {

        // basecase
        if (root == null) { 
            return null;
        }
        else {
            TreeNode left = invertTree(root.left);
            TreeNode right = invertTree(root.right);

            //swaps both subtrees
            root.left = right; 
            root.right = left; 

            return root;
        }
    }
}
Console
