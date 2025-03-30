class Solution:
    def minimumCandies(self, ratings):
        n = len(ratings)
        if n == 0:
            return 0
        
        # Step 1: Every child gets at least 1 candy
        candies = [1] * n

        # Step 2: Left to Right Pass
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        # Step 3: Right to Left Pass
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)

        # Step 4: Total candies
        return sum(candies)


# ✅ Example Usage
solution = Solution()
print(solution.minimumCandies([1, 0, 2]))     # Output: 5
print(solution.minimumCandies([1, 2, 2]))     # Output: 4