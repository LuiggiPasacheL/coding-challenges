
class Solution:

    def is_palindrome(self, number: int):

        if number < 0:
            return False
        
        number_len = self.len_number(number)

        for i in range(number_len // 2):

            right = number // (10 ** (number_len - i - 1)) % 10
            left = (number % (10**(i+1))) // (10**(i))

            if right != left:
                return False

        return True

    def len_number(self, number: int) -> int:

        len = 1

        while(number // (10**len) != 0):
            len += 1

        return len


print(Solution().is_palindrome(1234321)) # True
print(Solution().is_palindrome(456789987654)) # True
print(Solution().is_palindrome(1221)) # True
print(Solution().is_palindrome(123456)) # False
print(Solution().is_palindrome(123421)) # False
