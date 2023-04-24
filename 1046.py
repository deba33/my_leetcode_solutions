# Last Stone Weight
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """ 
        This code takes a list of integers representing the weights of stones. It repeatedly sorts the list in ascending order, subtracts the second-to-last element from the last element, and removes the second-to-last element. This process continues until there is only one stone left in the list. The function then returns the weight of the last remaining stone. This simulates the process of smashing two stones together and removing them if they are of equal weight, until only one stone remains. 


        Time: O(nlogn)
        Space: O(n)

        :param stones: List[int]
        :return: int
        """
        while len(stones) > 1:
            stones.sort()
            stones[-1] = stones[-1] - stones[-2]
            stones.pop(-2)
        return stones[0]
