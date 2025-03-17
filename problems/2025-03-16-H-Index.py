#Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, 
#return the researcher's h-index.

#According to the definition of h-index on Wikipedia: 
#The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times.

from typing import List

class Solution:
    def hIndex(self, citations :List[int]) ->int:
        #sort the list from the largetst to the smallest
        citations.sort(reverse=True)

        h = 0
        for i, c in enumerate(citations, start = 1):
            if c >= i:
                h = i
            else:
                break
        return h
    

def main():
    citations = [3,0,6,1,5]
    solution = Solution()

    h_index = solution.hIndex(citations)

    print("The H-index of the researcher will be:", h_index)

if __name__ == "__main__":
    main()