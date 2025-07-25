# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        pointer = len(digits) - 1

        digits[pointer] += 1
        
        while(digits[pointer] > 9):
            digits[pointer] = 0

            if pointer > 0:
                pointer -= 1
                digits[pointer] += 1
            else:
                digits.insert(0, 1)


        return digits
    
    def plusOneV2(self, digits: List[int]) -> List[int]:

        pointer = len(digits) - 1
        borrow = 0

        digits[pointer] = digits[pointer] + 1

        while(digits[pointer] >= 10):
            
            borrow = 1
            digits[pointer] -= 10
        
            pointer -= 1

            if pointer < 0:
                digits.insert(0, 1)
                break

            digits[pointer] += borrow
            borrow = 0

        return digits

print(Solution().plusOne([1,0,0]))
print(Solution().plusOne([1,2,9]))
print(Solution().plusOne([9,9,9]))

print(Solution().plusOneV2([1,0,0]))
print(Solution().plusOneV2([1,2,9]))
print(Solution().plusOneV2([9,9,9]))
print("finish")
