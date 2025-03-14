#You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].
#Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:
#0 <= j <= nums[i] and i + j < n
#Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].

from typing import List
class Solution:
    def jump(self, nums: List[int]) -> int:
        #we are using greedy algorithm to solve this
        #have two pointers, the left and the right
        #loop through the list twice while checking which option can lead us to the end of the list faster
        res = 0
        left = right = 0

        #loop through the list
        while right < len(nums) - 1:
            max_val = 0
            for i in range(left, right + 1):
                max_val = max(max_val, i + nums[i])
            left = right + 1
            right = max_val
            res += 1

        return res
    
def main():
    nums = [2,3,1,1,4]

    solution = Solution()

    min_steps = solution.jump(nums)
    print("Minimum steps required to reach the end of the list is:", min_steps)

if __name__ == "__main__":
    main()