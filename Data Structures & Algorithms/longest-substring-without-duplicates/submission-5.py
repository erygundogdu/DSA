class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        st = set()
        l = 0
        mx =0 
        for i in range(len(s)):
            if s[i] not in st:
                st.add(s[i])
            else:
                while s[i] in st:
                    st.remove(s[l])
                    l +=1
                st.add(s[i])
            mx = max(mx, i -l +1)
        return mx






        