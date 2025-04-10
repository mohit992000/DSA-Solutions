# ✅ Maximum Consecutive Ones After Flipping Zeroes - Sliding Window

class Solution:
    def longestOnes(self, arr, k):
        left = 0
        max_len = 0
        zeros = 0

        for right in range(len(arr)):
            if arr[right] == 0:
                zeros += 1

            while zeros > k:
                if arr[left] == 0:
                    zeros -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len


# ✅ Example usage
solution = Solution()
print(solution.longestOnes([1, 0, 1], 1))               # Output: 3
print(solution.longestOnes([1, 0, 0, 1, 0, 1, 0, 1], 2)) # Output: 5