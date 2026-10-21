class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        
        nums = sorted(nums)
        cnt = 0
        MOD = 10**9 + 7
        for i in range(len(nums)):
            l = i
            r = len(nums)-1
            while l <=r:
                m = (l+r) // 2
                if nums[m] + nums[i] <=target:
                    l = m+1
                else:
                    r = m-1
            if r>=i:
                cnt = (cnt + pow(2, r - i, MOD)) % MOD
        return cnt
            
            
        
        
        

            
        