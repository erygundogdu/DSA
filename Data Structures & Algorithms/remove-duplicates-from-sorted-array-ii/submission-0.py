class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 2
        for fast in range(2,len(nums)):
            if nums[fast] != nums[slow-2]:
                val = nums[slow]
                nums[slow] = nums[fast]
                nums[fast]=val
                slow+=1
        return slow



                



            
                   


                

            



        