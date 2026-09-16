class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        st1 = set("{[(")
        st2 = set(")]}")
        for c in s:
            if c in st1:
                stk.append(c)
            if c in st2:
                if stk == []:
                    return False
                ch = stk.pop()
                if ch == "(" and c != ")":
                    return False
                if ch == "[" and c != "]":
                    return False
                if ch == "{" and c != "}":
                    return False
        if stk != []:
            return False
        return True

        

            
        