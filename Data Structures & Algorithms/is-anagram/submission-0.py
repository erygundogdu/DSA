class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dct1 = {}
        for n in s:
            if n in dct1:
                dct1[n] +=1
            else:
                dct1[n] = 1
        dct2 = {}
        for c in t:
            if c in dct2:
                dct2[c] +=1
            else:
                dct2[c] = 1
        if set(dct1.keys()) == set(dct2.keys()):
            
            for k in s:
                if dct1[k] != dct2[k]:
                    return False
            return True
        return False
        
        
        