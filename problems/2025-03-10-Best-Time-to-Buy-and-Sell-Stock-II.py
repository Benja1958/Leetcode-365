#You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
#On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. 
#However, you can buy it then immediately sell it on the same day.

from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #Have a variable to store the profits
        #add to the profits only when the next price is higher thsn the previous one
        profits = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profits += (prices[i] - prices[i - 1])

        return profits
    
def main():
    prices = [7,1,5,3,6,4]

    solution = Solution()
    profit = solution.maxProfit(prices)

    print("The kax profit is:", profit)

if __name__ == "__main__":
    main()