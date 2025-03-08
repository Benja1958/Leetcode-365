#Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed.
# Then return the number of elements in nums which are not equal to val.
#Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:
#Change the array nums such that the first k elements of nums contain the elements which are not equal to val. 
#The remaining elements of nums are not important as well as the size of nums.
#Return k.

from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #mantain a left counter to swap elements when not equal to val
        left = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[left] = nums[i]
                left += 1

        return left
    

def main():
    nums = [3,2,2,3] 
    val = 3 

    solution = Solution()
    k = solution.removeElement(nums, val)
    print("Length of final elements not equal to val:", k)

if  __name__ == "__main__":
    main()

