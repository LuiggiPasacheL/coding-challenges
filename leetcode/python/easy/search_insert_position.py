# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        i = 0
        while(i < len(nums) and nums[i] < target):
            i += 1

        return i

    def searchInsert2(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums) - 1

        while(right != left):

            mid = (right + left) // 2

            if mid < 0:
                return 0

            if mid > len(nums):
                return len(nums)

            if nums[mid] == target:
                return mid

            if nums[mid] < target:
                # search in the right
                left = mid + 1
            else:
                # search on the left
                right = mid - 1

        return left + 1 if nums[left] < target else left
           

Solution().searchInsert2([1, 3], 0)        
