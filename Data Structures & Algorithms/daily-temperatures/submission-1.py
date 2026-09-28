class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stk = []
        for i in range(len(result)-1,-1,-1):
            cnt = 0
            while stk and temperatures[stk[-1]] <= temperatures[i]:
                stk.pop()
            if stk:
                result[i] = stk[-1] - i 
            stk.append(i)   
        return result


            

        