class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:

        ##O(n) sol

        small = []
        large = []
        out = []
        cnt = 0
        for n in nums:
            if n<pivot:
                small.append(n)
            elif n>pivot:
                large.append(n)
            else:
                cnt +=1
        small = small[::-1]
        large = large[::-1]
        while small:
            val  = small.pop()
            out.append(val)
        for _ in range(cnt):
            out.append(pivot)
        while large:
            val_l = large.pop()
            out.append(val_l)
        return out
        pass
