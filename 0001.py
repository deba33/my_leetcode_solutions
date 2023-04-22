# Two Sum
from typing import List
'''
This code implements the "Two Sum" problem, which asks to find two numbers in a given list that add up to a given target value. The function takes in a list of integers nums and an integer target, and returns a list of two integers that represent the indices of the two numbers in nums that add up to target.

'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        The function uses a dictionary d to store the indices of the numbers in nums. It iterates through nums using the enumerate function to get both the index and the value of each number. For each number j, it calculates the complement r of j with respect to target (i.e., r = target - j). If r is already in the dictionary d, it means that the complement of a previous number has been found, so the function returns the indices of the two numbers that add up to target. Otherwise, it adds the index of j to the dictionary d with j as the key. 
        
        The function returns an empty list if no two numbers add up to target. 
        
        Parameters
        ----------
        nums : List[int]
            A list of integers.
        target : int
            An integer.
        
        Returns
        -------
        List[int]
            A list of two integers.
        
        Examples
        --------
        >>> nums = [2,7,11,15]
        >>> target = 9
        >>> twoSum(nums, target)
        [0, 1]
        
        >>> nums = [3,2,4]
        >>> target = 6
        >>> twoSum(nums, target)
        [1, 2]
        
        >>> nums = [3,3]
        >>> target = 6
        >>> twoSum(nums, target)
        [0, 1]
        
        >>> nums = [3,3]
        >>> target = 6
        >>> twoSum(nums, target)
        [0, 1]
        
        >>> nums = [3,3]
        >>> target = 6
        >>> twoSum(nums, target)
        [0, 1]
        
        >>> nums = [3,3]
        
        Notes
        -----
        The function is implemented in the following steps:
        
        1. Create a dictionary d.
        2. Iterate through nums using the enumerate function.
        3. For each number j, calculate the complement r of j with respect to target (i.e., r = target - j).
        '''
        d = {}
        for i, j in enumerate(nums):
            r = target - j
            if r in d:
                return [d[r], i]
            d[j] = i


