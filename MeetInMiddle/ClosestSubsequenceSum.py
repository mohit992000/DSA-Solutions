import bisect

class Solution:
    def minAbsDifference(self, nums, target):
        def get_sub_sums(arr):
            # Generate all possible sums of subsets
            res = [0]
            for num in arr:
                res += [num + x for x in res]
            return res
        
        n = len(nums)
        left = nums[:n//2]
        right = nums[n//2:]
        
        left_sums = get_sub_sums(left)
        right_sums = sorted(get_sub_sums(right))
        
        ans = float('inf')
        for s in left_sums:
            remain = target - s
            idx = bisect.bisect_left(right_sums, remain)
            
            # Try the closest right sum (left and possibly one before)
            if idx < len(right_sums):
                ans = min(ans, abs(s + right_sums[idx] - target))
            if idx > 0:
                ans = min(ans, abs(s + right_sums[idx - 1] - target))
        
        return ans

# ✅ Example Usage
solution = Solution()
print(solution.minAbsDifference([5, -7, 3, 5], 6))  # Output: 0
print(solution.minAbsDifference([1, 2, 3], -7))     # Output: 7