class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:

        l = 0
        sm = 0
        for i in range(k):
            sm += arr[i]
        cnt = 0
        if sm >= threshold * k:
                cnt+=1
        for j in range(k,len(arr)):
            sm = sm - arr[l] + arr[j] 
            l +=1
            if sm >= threshold * k:
                cnt+=1
        return cnt





        