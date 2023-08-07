class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> list = new ArrayList<>();
        for (int i = 0; i < nums.length - 2; i++) {

            if (i > 0 && nums[i] == nums[i - 1])
                continue;
            
            int target = -1*(nums[i]);
            int j = i + 1;
            int k = nums.length - 1;
            while (j < k) {
                int sum = nums[j] + nums[k];
                if (sum == target) {
                    List<Integer> toAdd = Arrays.asList(nums[i], nums[j], nums[k]);
                    list.add(toAdd);
                    while (j < k && nums[j] == nums[j + 1])
                        j++;
                    while (j < k && nums[k] == nums[k - 1])
                        k--;
                    j++;
                    k--;
                }
                else if (sum < target)
                    j++;
                else 
                    k--;
            }
        }
        return list;
    }
}
