class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        lst_r = [1] * len(nums)
        lst_l = [1] * len(nums)
        lst = [1] * len(nums)
        for i in range(1,len(nums)):
            lst_r[i] = lst_r[i-1] * nums[i-1]
        for  j in range(len(nums)-2,-1,-1):
            lst_l[j] = lst_l[j+1] * nums[j+1]
        for k in range(len(nums)):
            lst[k] = lst_r[k] * lst_l[k]
        return lst
            
        