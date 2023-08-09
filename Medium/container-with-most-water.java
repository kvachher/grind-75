class Solution {
    public int maxArea(int[] height) {
        int left = 0; 
        int right = height.length - 1;
        int maxArea = 0; 
        while (right > left) {
            int area = Math.min(height[right], height[left])*(right - left);
            if (area > maxArea) {
                maxArea = area;
            }
            if (height[right] >= height[left]) {
                left++;
            }
            else {
                right--;
            }
        }
        return maxArea;
    }
}
