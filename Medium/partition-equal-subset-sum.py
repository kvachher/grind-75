class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        target = sum(nums) // 2
        dp = [False]*(target + 1)
        dp[0] = True

        if n == 1 or sum(nums) % 2 == 1: 
            return False
        if n == 2 : 
            return nums[0] == nums[1]
            
        for x in nums:
            if x > target:
                continue
            for s in range(target, x - 1, -1):
                if dp[s - x]:
                    dp[s] = True
            if dp[target]:
                return True

        return dp[target]
