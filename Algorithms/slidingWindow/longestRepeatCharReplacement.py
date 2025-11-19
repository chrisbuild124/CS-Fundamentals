# Longest Repeaeting Character Replacement
# Link: https://leetcode.com/problems/longest-repeating-character-replacement/description/

# This uses the sliding window technique to basically find the largest sliding window with the most 
# repeated characters that is valid

from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        vals = defaultdict(int)
        l = 0
        maxF = 0

        for r in range(len(s)):
            vals[s[r]] += 1
            if vals[s[r]] > maxF:
                maxF = vals[s[r]]

            while (r - l + 1) - maxF > k:
                vals[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res
            
