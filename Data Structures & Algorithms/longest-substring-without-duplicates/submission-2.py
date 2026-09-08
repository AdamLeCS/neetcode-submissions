class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # loop through string, anytime a duplicate is encountered, mark down max size and move
        # left pointer until that character is excluded
        if len(s) == 0 or len(s) == 1:
            return len(s)

        longest = 0
        l = 0
        r = 0
        chars = []
        while r < len(s):
            if s[r] not in chars:
                chars.append(s[r])
            else:
                longest = max(longest, r - l)
                while(s[r] != s[l]):
                    chars.remove(s[l])
                    l += 1
                l += 1
            r += 1
        
        return max(longest, r - l)

        