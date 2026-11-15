class Solution:
    def isValid(self, s: str) -> bool:
        st_o = set("{[(")
        st_c = set("}])")
        stk_o = []
        cnt = 0
        for c in s:
            if c in st_o:
                stk_o.append(c)
            if c in st_c:
                if not stk_o:
                    return False
            if stk_o and c in st_c:
                cnt +=1
                val = stk_o.pop()
                if val == "{":
                    if c != "}":
                        return False
                if val == "[":
                    if c != "]":
                        return False
                if val == "(":
                    if c != ")":
                        return False
        if cnt != 0 and len(stk_o) == 0:
            return True
        return False
                
            
        