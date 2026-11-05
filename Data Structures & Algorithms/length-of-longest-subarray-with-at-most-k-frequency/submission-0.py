class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:

        l = 0
        dct = {}
        mx = 0 
        for i in range(len(nums)):
            dct[nums[i]] = dct.get(nums[i],0)+1
            while dct and dct[nums[i]] > k:
                dct[nums[l]] -=1
                l+=1
            mx = max(mx,i-l+1)
            
        return mx
            
        pass
