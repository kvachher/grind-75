class Solution {
    public int[] productExceptSelf(int[] nums) {
        int p[] = new int[nums.length];
        int pre = 1; 
        int post = 1;
        for (int i = 0; i < nums.length; i++) {
            p[i] = pre;
            pre *= nums[i];
        }
        for (int j = nums.length - 1; j >= 0; j--) {
            p[j] *= post;
            post *= nums[j];
        }
        return p;
    }
}
