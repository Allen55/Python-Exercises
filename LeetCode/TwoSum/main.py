# Two Sum
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.


def two_sum(nums, target):

    low = 0
    high = len(nums) - 1

    while low < high:

        value = nums[low] + nums[high]

        if value != target:
            high = high - 1
        if low == high:
            low = low + 1
            high = len(nums) - 1




nums = [2, 7, 11, 15]
target = 18
# output [0,1]
print(two_sum(nums, target))