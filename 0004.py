from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        '''
        This code takes two sorted arrays, nums1 and nums2, and merges them into a single sorted array called nums. It then calculates the median of the merged array and returns it as a float. If the length of the merged array is even, it takes the average of the two middle elements. If the length is odd, it returns the middle element.
        
        Time Complexity: O(n)
        Space Complexity: O(n)
        
        :param nums1: List[int]
        :param nums2: List[int]
        :return: float
        '''
        nums = nums1 + nums2
        nums.sort()
        if len(nums) % 2 == 0:
            return (nums[len(nums) // 2] + nums[len(nums) // 2 - 1]) / 2
        else:
            return nums[len(nums) // 2]