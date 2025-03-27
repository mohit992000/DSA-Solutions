class Solution:
    def longestConsecutive(self, nums):
        # Convert the list to a set for O(1) lookups
        num_set = set(nums)
        longest = 0

        # Go through each number in the set
        for num in num_set:
            # Only start counting if `num - 1` is not in the set
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                # Count how many consecutive numbers exist starting from current_num
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                # Update longest streak found so far
                longest = max(longest, current_streak)

        return longest


# ✅ Example Usage:
solution = Solution()
print(solution.longestConsecutive([100, 4, 200, 1, 3, 2]))       # Output: 4
print(solution.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1])) # Output: 9
print(solution.longestConsecutive([1, 0, 1, 2]))                 # Output: 3