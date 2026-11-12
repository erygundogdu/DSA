class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        
        
        intervals.sort(key=lambda x: x[0])
        prevend = intervals[0][1]

        cnt = 0
        i = 1
        for i in range(1, len(intervals)):
            if intervals[i][0] < prevend:
                cnt +=1 
                prevend = min(prevend, intervals[i][1])
            else:
                prevend = intervals[i][1]
        return cnt




        