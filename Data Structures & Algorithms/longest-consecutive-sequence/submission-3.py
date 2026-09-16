class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        val = 0
        cnt = 0 
        mx = -1
        st = set(nums)
        if len(nums) == 0:
            return 0
        for i in range(len(nums)):
            if nums[i] -1 not in st:
                cnt = 1
                val = nums[i]
                while val in st:
                    cnt +=1
                    val +=1      
            if cnt > mx:
                mx = cnt
            cnt = 1
        return mx -1



        
             

        


        