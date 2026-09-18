class Solution:

    def encode(self, strs: List[str]) -> str:
        s =""
        for i in range(len(strs)):
            s = s + "ğ" + strs[i]
        s  = s +"ğ"
        return s

    def decode(self, s: str) -> List[str]:
        lst = []
        cnt = 0
        val = "ğ"
        for i,c in enumerate(s) :
            if c == val:
                lst.append(i)
        lst_s = []
        for j in range(1,len(lst)):
            lst_s.append(s[lst[j-1]+1:lst[j]])
        return lst_s

           
                

        


        


