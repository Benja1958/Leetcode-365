#Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

from typing import List
class Solution:
    def rotate(self, nums: List[int], k : int) -> None:
        #reverse the list first
        #reverse the first k elements, then after that reverse the rest of the elements after k
        k = k % len(nums)

        #reverse the array first
        l, r = 0, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

        #reverse the first k elements
        l, r = 0, k - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        
        #reverse the rest elements after k
        l, r = k, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        return nums


def main():
    nums = nums = [1,2,3,4,5,6,7]
    k = 3
    
    solution = Solution()
    result = solution.rotate(nums, k)

    print("The new rotated list will be:", result)

if __name__ == "__main__":
    main()
