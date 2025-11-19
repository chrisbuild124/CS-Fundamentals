# Longest Substring Without Repeating Characters
# Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

# The trick here is to constantly expand the window right and save each iteration right the largest
# possible window size into the result.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0
        l, r = 0, 0
        letters = set()
        while r < len(s):
            while s[r] in letters:
                letters.remove(s[l])
                l += 1
            count = max(count, r - l + 1)
            letters.add(s[r])
            r += 1
        
        return count 
