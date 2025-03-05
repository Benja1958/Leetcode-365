#You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
#Merge nums1 and nums2 into a single array sorted in non-decreasing order.
#The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, 
#nums1 has a length of m + n, where the first m elements denote the elements that should be merged, 
#and the last n elements are set to 0 and should be ignored. nums2 has a length of n

from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #since the arrays are sorted, we can start checking from the their non_zero ends
        #then append the greatest elements starting from the end of nums1
        #loop through the two arrays while comparing

        len_total = n + m - 1
        m = m - 1
        n = n - 1

        while n >= 0:
            if m >= 0 and nums1[m] > nums2[n]:
                nums1[len_total] = nums1[m]
                m -= 1
            else:
                nums1[len_total] = nums2[n]
                n -= 1
            len_total -= 1


def main():
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6] 
    n = 3

    solution  = Solution()
    solution.merge(nums1, m, nums2, n)

    print("Merged array:", nums1) 

if  __name__ == "__main__":
    main()
