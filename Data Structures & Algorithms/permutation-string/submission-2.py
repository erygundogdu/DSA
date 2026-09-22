class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        w = len(s1)
        if w > len(s2):
            return False
        target = {}
        window = {}
        for c in s1:
            target[c] = target.get(c, 0) + 1
        for c in s2[:w]:
            window[c] = window.get(c, 0) + 1
        if window == target:
            return True

        for i in range(w,len(s2)):

            window[s2[i]] = window.get(s2[i], 0) +1
            old = s2[i-w]
            window[old] -=1
            if window[old] == 0:
                del window[old]
            if window  == target :
                return True
        return False

            

                
