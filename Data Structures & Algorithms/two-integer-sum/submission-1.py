class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dct = {}
        for i,n in enumerate(nums):
            dct[n] = i

        for j in range(len(nums)):
            if target - nums[j] in dct and j != dct[target-nums[j]]:
                return [j,dct[target-nums[j]]]
        return []

        