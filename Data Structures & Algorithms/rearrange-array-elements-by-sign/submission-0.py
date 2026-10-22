class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:

        out = []
        stk_pos = []
        stk_neg = []
        for i in range(len(nums)):
            if nums[i] >=0:
                stk_pos.append(nums[i])
            else:
                stk_neg.append(nums[i])
        while stk_neg or stk_pos:
            neg = stk_neg.pop()
            pos = stk_pos.pop()
            out.append(neg)
            out.append(pos)
        return out[::-1]
        


        