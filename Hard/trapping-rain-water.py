class Solution(object):
    def trap(self, height):
        l = 0
        r = len(height) - 1
        maxL = height[l]
        maxR = height[r]
        sum = 0
        while (l < r) : 
            if maxL > maxR :
                r -= 1
                if (min(maxL, maxR) - height[r] > 0) :
                    sum += min(maxL, maxR) - height[r]
                maxR = max(maxR, height[r])
            else :
                l += 1
                if (min(maxL, maxR) - height[l]) > 0 :
                    sum += min(maxL, maxR) - height[l]
                maxL = max(maxL, height[l])
        return sum
