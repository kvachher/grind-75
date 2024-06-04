class Solution:
    # first find pivot -> split into two lists i think
    # sort both lists
    def search(self, nums: List[int], target: int) -> int:
        pivot = 0
        l, r = 0, len(nums) - 1
        while (l < r) : 
            m = (l + r) // 2
            if nums[m] > nums[r] : 
                l = m + 1
            else : 
                r = m

        pivot = l

        # searching partitioned lists
        l1 = nums[0:pivot]
        l2 = nums[pivot:]
        ans1 = self.recurse(l1, 0, len(l1) - 1, target)
        ans2 = self.recurse(l2, 0, len(l2) - 1, target)

        if (ans1 == -1 and ans2 == -1) : 
            return -1
        elif (ans1 == -1) : 
            return len(l1) + ans2
        else : 
            return ans1

    # binary search
    def recurse(self, arr, low, high, target):
            if (high >= low) : 
                mid = (high + low) // 2
                if (arr[mid] == target) : 
                    return mid
                elif (arr[mid] > target): 
                    return self.recurse(arr, low, mid-1, target)
                elif (arr[mid] < target): 
                    return self.recurse(arr, mid+1, high, target)
            else:
                return -1
