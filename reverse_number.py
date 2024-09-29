"""
7. Reverse Integer
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
 

Constraints:

-231 <= x <= 231 - 1
"""

class Solution:
    def reverse(self, x: int) -> int:
        def reverse(no):
            temp = no
            reverse = 0
            while temp > 0:
                rem = temp % 10
                reverse = reverse * 10 + rem
                temp = temp // 10
            return reverse

        if x > 0:
            reverse_no = reverse(x)
            if reverse_no > (2 ** 31):
                return 0
            return reverse_no
        else:
            no = (-1) * x
            reverse_no = reverse(no)
            if reverse_no > (2 ** 31):
                return 0
            reverse_no = (-1) * reverse_no
            return reverse_no



















# x = 1534236469

# def reverse(no):
#     temp = no
#     reverse = 0
#     while temp > 0:
#         rem = temp % 10
#         reverse = reverse * 10 + rem
#         temp = temp // 10
#     return reverse

# if x > 0:
#     reverse_no = reverse(x)
#     if reverse_no > (2 ** 31):
#         return 0

# # else:
#     no = (-1) * x
#     reverse_no = reverse(no)
#     if reverse_no > (2 ** 31):
#         return 0
    
#     reverse_no = (-1) * reverse_no