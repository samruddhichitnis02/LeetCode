"""2217. Find Palindrome With Fixed Length
Attempted
Medium
Topics
Companies
Hint
Given an integer array queries and a positive integer intLength, return an array answer where answer[i] is either the queries[i]th smallest positive palindrome of length intLength or -1 if no such palindrome exists.

A palindrome is a number that reads the same backwards and forwards. Palindromes cannot have leading zeros.

 

Example 1:

Input: queries = [1,2,3,4,5,90], intLength = 3
Output: [101,111,121,131,141,999]
Explanation:
The first few palindromes of length 3 are:
101, 111, 121, 131, 141, 151, 161, 171, 181, 191, 202, ...
The 90th palindrome of length 3 is 999.
Example 2:

Input: queries = [2,4,6], intLength = 4
Output: [1111,1331,1551]
Explanation:
The first six palindromes of length 4 are:
1001, 1111, 1221, 1331, 1441, and 1551.
 

Constraints:

1 <= queries.length <= 5 * 104
1 <= queries[i] <= 109
1 <= intLength <= 15
"""

class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        exp_start = 10 ** (intLength - 1)
        dig = len(str(abs(max(queries))))
        if dig > intLength:
            exp_end = (10 ** dig) 
        else:
            exp_end = 10 ** intLength

        pal_lis= []
        pal_lis_ret = []

        def is_palindrome(no):
            return str(no) == str(no)[::-1]

        for num in range(exp_start, exp_end):
            if is_palindrome(num):
                pal_lis.append(num)

        pal_lis_ret = [pal_lis[i - 1] for i in queries]

        return pal_lis_ret
        






# n = 1
# queries = [2,201429812,8,520498110,492711727,339882032,462074369,9,7,6]

# exp_start = 10 ** (n - 1)
# dig = len(str(abs(max(queries))))

# if dig > n:
#     exp_end = (10 ** dig) 
# else:
#     exp_end = 10 ** n

# pal_lis= []
# pal_lis_ret = []


# def is_palindrome(no):
#     return str(no) == str(no)[::-1]

# for num in range(exp_start, exp_end):
#     if is_palindrome(num):
#         pal_lis.append(num)

# pal_lis_ret = [pal_lis[i - 1] for i in queries]

# print(pal_lis_ret)