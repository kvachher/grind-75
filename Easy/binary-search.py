class Solution(object):
    def search(self, nums, target):
        return self.search_helper(nums, 0, len(nums) - 1, target)
    
    def search_helper (self, arr, low, high, target):
        i = 0
        if (high >= low) : 
            mid = (high + low) // 2
            if (arr[mid] == target) : 
                return mid
            elif (arr[mid] > target): 
                return self.search_helper(arr, low, mid-1, target)
            elif (arr[mid] < target): 
                return self.search_helper(arr, mid+1, high, target)
        else:
            return -1
