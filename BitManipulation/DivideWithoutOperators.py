# ✅ Divide Two Integers Without Using / * %

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # Edge case: overflow
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        # Determine sign of the result
        negative = (dividend < 0) != (divisor < 0)

        # Work with absolute values
        dividend = abs(dividend)
        divisor = abs(divisor)

        quotient = 0

        while dividend >= divisor:
            temp = divisor
            multiple = 1

            # Find the highest double of divisor that fits into dividend
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1

            # Subtract the largest found chunk
            dividend -= temp
            quotient += multiple

        return -quotient if negative else quotient


# 🧪 Example test
solution = Solution()
print(solution.divide(10, 3))   # Output: 3
print(solution.divide(7, -3))   # Output: -2
print(solution.divide(-1, 1))   # Output: -1