# Longest palindrome substring 
# Link: https://leetcode.com/problems/longest-palindromic-substring/description/

# Trick: To use two pointers to look both ways, this is worst n^2 (brute force is 2^n)


class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Two pointers
        res = s[0]

        for i in range(len(s)):
            # odd
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r-l+1 > len(res):
                    res = s[l:r+1]
                l, r = l-1, r+1

            # even
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r-l+1 > len(res):
                    res = s[l:r+1]
                l, r = l-1, r+1

        return res
