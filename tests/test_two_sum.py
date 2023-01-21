import unittest
from leetcode.two_sum import two_sum

# https://leetcode.com/problems/two-sum/
# Given an array of integers,
# return indices of the two numbers such that they add up to a specific target.

# You may assume that each input would have exactly one solution,
# and you may not use the same element twice.

# Constaints:
# 2 <= nums.length <= 10^4
# -10^9 <= nums[i] <= 10^9
# -10^9 <= target <= 10^9
# Only one valid answer exists.


class TestTwoSum(unittest.TestCase):

    def test_sum_of_output(self):
        # arrange
        nums = [2, 11, 7, 15]
        target = 9

        # act
        output = two_sum(nums, target)
        first_index = output[0]
        second_index = output[1]
        summed_output = nums[first_index] + nums[second_index]

        # assert
        self.assertEqual(summed_output, target)

    def test_length_of_output(self):
        # arrange
        nums = [23, -7, 11, 3, 5]
        target = 14

        # act/assert
        output = two_sum(nums, target)

        # assert
        self.assertEqual(len(output), 2)
