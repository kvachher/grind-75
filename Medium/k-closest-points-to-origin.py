class Solution(object):
    def kClosest(self, points, k):
        heap = []
        ans = []
        for p in points :
            heappush(heap, [math.sqrt((math.pow(p[0], 2)) + (math.pow(p[1], 2))), p])
        while k != 0 and heap: 
            ans.append(heappop(heap)[1])
            k -= 1
        return ans
