class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dct  = {}
        for n in nums:
            if n in dct:
                dct[n] +=1
            else:
                dct[n] = 1
        mx_lst = []
        while k >0:
            mx = -1
            for s in dct:
                if dct[s] > mx:
                    mx = dct[s]
                    val = s
            dct.pop(val,mx)
            mx_lst.append(val)
            k-=1
        return mx_lst
        



        


        