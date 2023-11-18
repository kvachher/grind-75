class Solution(object):
    def permute(self, nums):
        def backtrack(nums, temp, ans) :
            if not nums: 
                ans.append(temp)
                return
            for i in range(len(nums)):
                backtrack(nums[:i]+nums[i+1:], temp + [nums[i]], ans)
        ans = []
        backtrack(nums, [], ans)
        return ans
