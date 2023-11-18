class Solution(object):
    def subsets(self, nums):
        def backtrack(nums, ans) :
            if nums and nums not in ans : 
                ans.append(nums)
            for i in range(len(nums)) : 
                backtrack(nums[:i] + nums[i+1:], ans)
        ans = [[]]
        backtrack(nums, ans)
        return ans
