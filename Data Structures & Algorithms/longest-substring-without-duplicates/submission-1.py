class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        i=0
        char_dict = {}
        for j in range(len(s)):
            if s[j] in char_dict.keys():
                i = max(i,char_dict[s[j]]+1)
            char_dict[s[j]] = j
            ans = max(ans,j-i+1)
        return ans


            


        