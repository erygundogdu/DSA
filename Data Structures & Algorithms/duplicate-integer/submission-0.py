class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        st = set(nums)
        cnt = 0
        val = 0
        for n in nums:
            if n in st:
                st.remove(n)
            else:
                return True
        return False

        