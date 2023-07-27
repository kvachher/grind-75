class Solution {
    public int majorityElement(int[] nums) {
        HashMap<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            if (map.containsKey(nums[i])) {
                int occ = map.get(nums[i]);
                map.put(nums[i], occ+1);
            }
            else 
                map.put(nums[i], 1);
            
            if (map.get(nums[i]) > (nums.length / 2))
                return nums[i];
        }
    return -1; 
    }
}
