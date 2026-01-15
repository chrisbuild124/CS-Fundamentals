# Reverse Integer 
# Link: https://leetcode.com/problems/reverse-integer/description/

# Use addition and checking digits for overflow error, and use
# fmod from python to help compute digits (so it doesn't error out). 
# Use x = int(x/10) because int rounds down to 0, rather than x // 10. 

class Solution:
    def reverse(self, x: int) -> int:
        MIN = -1 * (2 ** 31)
        MAX = 2 ** 30 + ((2 ** 30) - 1)
        res = 0

        while x:
            dig = int(math.fmod(x, 10))
            x = int(x / 10)

            if res > MAX // 10 or (res == MAX // 10 and dig > MAX % 10):
                return 0
            if res < MIN // 10 or (res == MIN // 10 and dig < MAX % 10):
                return 0
            res = res * 10 + dig
        
        return res
