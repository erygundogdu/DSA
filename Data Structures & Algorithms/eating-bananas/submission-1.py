class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
            mx = max(piles)
            mn = 1
            while mn <= mx:
                hour = 0
                k = (mn + mx) // 2
                for pile in piles:
                    hour = hour + (pile + k - 1) // k
                if hour > h:
                    mn = k+1
                else :
                    mx = k-1
            return mn 
                






        
                    

                    




        