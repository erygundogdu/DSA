class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:

        arr = customers[0][0]
        wait = customers[0][1]
        t = arr + wait
        for i in range(1,len(customers)):
            if t > customers[i][0]:
                rem = t-customers[i][0]
                wait = wait + rem + customers[i][1]
                t = t + customers[i][1]
            else:
                wait = wait + customers[i][1]
                t = customers[i][0] + customers[i][1] 
        return wait/len(customers)

            

            
        