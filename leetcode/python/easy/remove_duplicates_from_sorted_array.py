from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        stack = [nums[0]]

        for num in nums:
            if stack[-1] != num:
                stack.append(num)

        nums = stack

        return len(stack)
            

lists = [
    [1,1,2],
    [0,0,1,1,1,2,2,3,3,4]
]

for l in lists:
    Solution().removeDuplicates(l)
