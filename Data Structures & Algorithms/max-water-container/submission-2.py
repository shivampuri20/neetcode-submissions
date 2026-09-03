class Solution:
    def maxArea(self, heights: List[int]) -> int:
        r = len(heights)-1
        l =0

        sum =0

        while l<r:
            diff=r-l
            sum = max(sum , diff * min(heights[l], heights[r]))

            if heights[l] < heights[r]:
                l+=1
            elif heights[l] >= heights[r]:
                r=r-1
        return sum
        