class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mn = 10e8
        best_p = 0
        for p in prices :
            if p < mn:
                mn = p
            elif p -mn > 0 :
                best_p = max(best_p,p-mn)
        return best_p

        
            

        