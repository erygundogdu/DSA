class Solution:
    def maxArea(self, heights: List[int]) -> int:
            b_area = 0
        #for r in range(len(heights)-1,-1,-1):
            l = 0
            r = len(heights) -1 
            while l < r:
                area = min(heights[l],heights[r]) * (r-l)
                b_area = max(area, b_area)

                if area <= b_area:
                    if heights[l] < heights[r]:
                        l +=1
                    else:
                        r -=1
            return b_area
            
        