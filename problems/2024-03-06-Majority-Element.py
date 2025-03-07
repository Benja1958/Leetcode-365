#Given an array nums of size n, return the majority element.
#The majority element is the element that appears more than ⌊n / 2⌋ times. 
#You may assume that the majority element always exists in the array.

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #have  acounter to keep how many times an element appears
        #have a variable to store the current max appearing element
        #if current not equal to max element, reduce count by 1
        #if they are equal, add one
        

        count = 1
        num = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == num:
                count += 1
            elif count == 0:
                num = nums[i]
            else:
                count -= 1

        return num
    

def main():
    nums = [2,2,1,1,1,2,2]

    solution = Solution.majorityElement(nums)

    print("The majority element")