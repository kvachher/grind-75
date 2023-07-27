class Solution(object):
    def maxSubArray(self, nums):
        sums = [0]*len(nums)
        sums[0] = nums[0]
        largest = sums[0]
        for i in range(1, len(nums)) :
            curr_sum = nums[i] + sums[i-1]
            if curr_sum > nums[i] :
                sums[i] = curr_sum
            else : 
                sums[i] = nums[i]
            if sums[i] > largest :
                largest = sums[i]
        
        return largest
