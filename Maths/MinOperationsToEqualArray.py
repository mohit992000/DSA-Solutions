# ✅ Minimum Operations to Make Array Equal by Incrementing n-1 Elements

class Solution:
    def minOperations(self, arr):
        min_val = min(arr)
        return sum(arr) - len(arr) * min_val


# ✅ Example usage
solution = Solution()
print(solution.minOperations([1, 2, 3]))     # Output: 3
print(solution.minOperations([4, 3, 4]))     # Output: 2
print(solution.minOperations([5, 5, 5, 5]))  # Output: 0