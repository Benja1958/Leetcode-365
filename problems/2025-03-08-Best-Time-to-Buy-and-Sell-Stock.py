#You are given an array prices where prices[i] is the price of a given stock on the ith day.
#You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
#Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #use two pointer one to track the low prices and the other one to track the high prices
        #initialize a max counter to store the max profits

        max_profit = 0
        low = 0

        #loop throught the index of the prices
        for i in range(len(prices)):
            if prices[i] > prices[low]:
                diff =  prices[i] - prices[low]
                max_profit = max(diff, max_profit)
            else:
                low = i

        return max_profit


def main():
    prices = [7,1,5,3,6,4]

    solution  = Solution()
    max_profits = solution.maxProfit(prices)

    print("The maximum profits will be:", max_profits)

if __name__ == "__main__":
    main()
