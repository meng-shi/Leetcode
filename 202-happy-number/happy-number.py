class Solution:
    def isHappy(self, n: int) -> bool:
        num = set()

        while n not in num:
            num.add(n)
            n = self.sum_of_square(n)
            if n == 1:
                return True
        return False

    def sum_of_square(self, n: int) -> int:
        output = 0
        while n > 0:
            digit = n % 10
            output += digit ** 2
            n = n // 10
            print(n)
        return output


