# Euclidean algorithm
# Link: https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/

# Trick here is to find the greatest common divisor using euclidean alg in logn time

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def getGCD(num1, num2):
            while num2 > 0:
                num1, num2 = num2, num1 % num2
            return num1

        p1, p2 = head, head.next
        while p1:
            if not p2:
                return head
            num = getGCD(p1.val, p2.val)
            p1.next = ListNode(num)
            p1.next.next = p2
            p1 = p2
            p2 = p2.next

        return head
