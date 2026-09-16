class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        mx = 0

        for val in set(s): 
            cnt = 0
            l = 0

            for i in range(len(s)):

                if s[i] != val:
                    cnt += 1

                while cnt > k:
                    if s[l] != val:
                        cnt -= 1
                    l += 1
                mx = max(mx, i - l + 1)
        return mx