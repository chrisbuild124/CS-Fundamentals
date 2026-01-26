# Happy number
# Link: https://leetcode.com/problems/happy-number/description/

# The trick is to use fast and slow pointers to see if there is a cycle
# Also another trick is to mod the digits instead of using //10
# since the runttime will be faster. 
class Solution:
    def isHappy(self, n: int) -> bool:   
        num1 = n
        num2 = n

        def helper(num):
            tmp = 0
            while num:
                tmp += (num % 10) ** 2
                num = num // 10
            return tmp

        while num2 != 1:
            num2 = helper(num2)
            num2 = helper(num2)
            num1 = helper(num1)
            if num2 == 1:
                break
            if num2 == num1:
                return False
        
        return True
