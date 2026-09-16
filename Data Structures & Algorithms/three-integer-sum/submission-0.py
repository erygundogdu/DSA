class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        dct = {}
        for i,n in enumerate(nums):
            dct[n] = i
        lst = []
        for j in range(len(nums)):
            for k in range(j+1,len(nums)):
                sm = nums[j] + nums[k]
                if -1 * sm in dct:
                    if dct[-1*sm] != j and dct[-1*sm] != k:
                        lst.append([-1*sm,nums[j],nums[k]])
        res = set()
        for sub_lst in lst:
            sub_lst = tuple(sorted(sub_lst))
            res.add(sub_lst)
        return [list(x) for x in res]
        

                        

        