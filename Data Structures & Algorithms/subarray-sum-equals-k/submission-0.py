class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        
        prefix_dct = {}
        p_sum = 0
        prefix_dct[p_sum] = 1
        count = 0 
        for i in range(len(nums)):
            p_sum += nums[i]
            if p_sum - k in prefix_dct:
                count+=prefix_dct[p_sum-k]
            if p_sum in prefix_dct:
                prefix_dct[p_sum] += 1
            else:
                prefix_dct[p_sum] = 1
        return count
            
                


        