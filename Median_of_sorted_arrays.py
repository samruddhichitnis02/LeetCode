"""
iven two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
"""
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # appending the 2nd list to 1st one
        nums1.extend(nums2)

        # sorting the list 1 after appending the 2nd list to it
        n = len(nums1) - 1
        for i in range(n * n):
            pos = i % n
            if nums1[pos] > nums1[pos + 1]:
                nums1[pos], nums1[pos + 1] = nums1[pos + 1], nums1[pos]

        # after sorting if the length of the array is odd then
        if len(nums1) % 2 != 0:
            return (nums1[int(len(nums1) / 2)])
        
        # after sorting if the length of the array is even then
        else:
            return ((nums1[len(nums1) // 2] + nums1[len(nums1) // 2 - 1]) / 2)



    
