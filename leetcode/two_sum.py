from typing import List

# https://leetcode.com/problems/two-sum/
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Constraints:
# 2 <= nums.length <= 10^4
# -10^9 <= nums[i] <= 10^9
# -10^9 <= target <= 10^9
# Only one valid answer exists.

def two_sum(nums: List[int], target: int) -> List[int]:
    '''returns the indexes of two ints that sum to target'''
    num_to_index_map = {}
    for idx, num in enumerate(nums):
        diff = target - num
        if diff in num_to_index_map:
            return [num_to_index_map[diff], idx]
        num_to_index_map[num] = idx
    return [-1, -1]
