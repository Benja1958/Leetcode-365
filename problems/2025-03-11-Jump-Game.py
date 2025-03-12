#You are given an integer array nums. You are initially positioned at the array's 
#first index, and each element in the array represents your maximum jump length at that position.
#Return true if you can reach the last index, or false otherwise.

from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #iterate through the index of the items in the array
        #initialize a goal variable to make sure you don't go out of index

        goal = 0
        for i in range(len(nums)):
            if goal < i:
                return False

            goal = max(goal, i + nums[i])
        return True
    
def main():
    nums = [2,3,1,1,4]

    solution = Solution()
    boolean = solution.canJump(nums)

    print(boolean,":to if you can reach the last index")

if __name__ == "__main__":
    main()