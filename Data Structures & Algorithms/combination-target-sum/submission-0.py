class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:


        res = []
        path = []
        def search(i):
            if i == len(nums):
                return 
            if sum(path) == target:
                res.append(path.copy())
            if sum(path) > target:
                return
            for j in range(i,len(nums)):
                path.append(nums[j])
                search(j)
                path.pop()
        search(0)
        return res



        