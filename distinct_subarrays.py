from typing import List

class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        seen = set()  # To store distinct subarrays as tuples.
        n = len(nums)
        
        # Outer loop: starting index of subarray.
        for i in range(n):
            count_divisible = 0
            # Inner loop: ending index of subarray.
            for j in range(i, n):
                if nums[j] % p == 0:
                    count_divisible += 1
                # If the count exceeds k, break early.
                if count_divisible > k:
                    break
                # Add the valid subarray (as tuple) to the set.
                seen.add(tuple(nums[i:j+1]))
        
        return len(seen)

# Example usage:
if __name__ == "__main__":
    sol = Solution()
    print(sol.countDistinct([2,3,3,2,2], 2, 2))  # Expected output: 11
    print(sol.countDistinct([1,2,3,4], 4, 1))    # Expected output: 10
