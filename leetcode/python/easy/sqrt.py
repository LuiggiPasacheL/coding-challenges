class Solution:
    def mySqrt(self, x: int) -> int:
        
        i = 1
        while(True):
            n = i ** 2

            if (x < n):
                return i - 1

            i += 1

    def mySqrt2(self, x: int) -> int:

        if x == 0 or x == 1:
            return x

        if x == 2:
            return x

        for i in range(1,x):
            if (x / i < i):
                return i - 1

        return 1


    def mySqrt3(self, x: int) -> int:

        if x == 0 or x == 1:
            return x

        start, end = 0, x
        middle = 0

        while(start <= end):
            
            middle = (start + end) // 2

            if middle ** 2 == x:
                return middle
            elif middle ** 2 > x:
                end = middle - 1
            else:
                start = middle + 1

        return middle


