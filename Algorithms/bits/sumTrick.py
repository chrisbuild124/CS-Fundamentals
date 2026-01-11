# Adding two numbers trick with bits, it also works with negative values. 
# Link: https://leetcode.com/problems/sum-of-two-integers

# Basically, mask will keep lower 32 bits and max is used to convert back to signed.
# NOTE: mask and MAX are needed in python but in other languages. Python does
# not have a maximum bit amount, but other languages do. That's why this constaint
# is needed. 

class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF # Keeps lower 32 bits at each step
        MAX = 0x7FFFFFFF # Helps convert a negative number back to signed

        carry = (a & b) & mask
        res = (a ^ b) & mask

        while carry:
            carry = (carry << 1) & mask
            tmp = res
            res = (res ^ carry) & mask
            carry &= tmp

        return res if res <= MAX else ~(res ^ mask)
