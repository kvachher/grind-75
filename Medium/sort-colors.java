class Solution {
    public void sortColors(int[] nums) {
        int zerocount = 0; 
        int onecount = 0; 
        int twocount = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 0)
                zerocount++;
            if (nums[i] == 1)
                onecount++;
            if (nums[i] == 2)
                twocount++;
        }
        int j = 0;
        while (zerocount > 0) {
            nums[j] = 0;
            j++;
            zerocount--;
        }
        while (onecount > 0) {
            nums[j] = 1;
            j++;
            onecount--;
        }
        while (twocount > 0) {
            nums[j] = 2;
            j++;
            twocount--;
        }
    }
}
