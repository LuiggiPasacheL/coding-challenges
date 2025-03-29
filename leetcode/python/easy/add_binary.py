class Solution:
    def addBinary(self, a: str, b: str) -> str:

        pointerA = len(a) - 1
        pointerB = len(b) - 1

        result = ""

        borrow = 0

        while (pointerA >= 0 or pointerB >= 0 or borrow != 0):

            valueA = 0
            if pointerA >= 0:
                valueA = a[pointerA]
            
            valueB = 0
            if pointerB >= 0:
                valueB = b[pointerB]
            
            value = int(valueA) + int(valueB) + borrow

            if (value >= 2):
                borrow = 1
                value = value - 2
            else:
                borrow = 0

            result = str(value) + result

            pointerB -= 1
            pointerA -= 1

        return result


print(Solution().addBinary("11","1"))
print("finish")
